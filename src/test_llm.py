'''This script enriches the current structured output by calling an LLM to assist with annotation.
It loops through the initial JSON data and returns a list of dictionaries with further annotated records.'''

# Eventually the output should look something like the following: 
'''
id: 1, 
text: ... 
verb: ... 
matched_span: ... 
noun predicate: ... 
left context: ... 
right context: ... 
is_candidate_lvc: ... 
'''

import json
import requests 
import copy
from dotenv import load_dotenv
import os

INPUT_FILE = "data/interim/verb_candidates.json"
OUTPUT_FILE = "data/processed/verbs_annotated.json"

# Set up CONFIGS for API
LLM_API_URL = os.getenv("LLM_API_URL")
LLM_MODEL = os.getenv("LLM_MODEL") #e.g., gemma-4-31B-it, llama-4-scout


# GET API / SECRET KEY
load_dotenv()
LLM_API_KEY = os.getenv("API_KEY")


def load_single_record():
    '''Load different lines of the candidate file to pass individually to model'''
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)
    
    # change which line here 
    return records[8] 


def call_llm(prompt): 
    '''Send request to specified LLM and return response as JSON.'''

    # sends auth to REALLMS
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}", 
        "Content-Type": "application/json", 
    }

    # request sent to the model
    # messages = chat format
    payload = {
        "model": LLM_MODEL, 
        "messages": [
            {"role": "system", "content": "Return JSON only."}, # instructions
            {"role": "user", "content": prompt}, # task
        ],
        "temperature": 0, # temperature 0 is rec'd for more predictable + focused responses
    }

    response = requests.post(LLM_API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status() # error handling

    # Return model response
    return response.json()

def parse_llm_response(content): 
    '''Remove triple backticks if present, and parse model JSON output.'''
    content = content.strip() 

    # remove code fences -- triple backticks ``` -- if they are present
    if content.startswith("```"): 
        content = content.strip("`")
        content = content.strip() 

        # also remove if it starts with '```json'
        if content.startswith("json"): 
            content = content[4:].strip() 

    content = json.loads(content)

    # Catch if the model returns a list instead of a dict
    if isinstance(content, list): # check if response is type list
        content = content[0]
        
    return content

def build_prompt(text, verb_surface, left_context, right_context): 
    '''This is the prompt that gets shown to the model'''

    # write prompt
    return f"""You are extracting Spanish light verb constructions. 

    Positive examples: 
    Positive examples typically can be paraphrased by a synthetic verb.
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE
    Hacer una elección. → TRUE
    Hace frío. → TRUE
    Los estudiantes hacen preguntas. → TRUE
    
    Negative examples:
    Negative examples typically have full semantic weight of the verb and parts of speech like subject (agent/source), direct object (theme/patient), indirect object (recipient/beneficiary).
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE
    Hizo un bizcocho. → FALSE
    Siempre hace la misma cosa. → FALSE
    Les digo lo que tengan que hacer. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - left_context
    - right_context
    - matched_span
    - verb_predicate
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - synthetic_paraphrase
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = TRUE if the verb_predicate carries more meaning than the verb, and the verb is used in a way other than its prototypical meaning.
    Mark is_lvc = FALSE if the verb contributes only tense, mood, or aspect and no semantic meaning (e.g., "tienes que estudiar").
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""
    - synthetic_paraphrase = ""
    - predicate_type = ""
    - predicate_aspect = ""

    For type_reason, explain is_lvc in 200 characters or less.
    If is_lvc = FALSE, explain parts of speech (e.g., indirect object or recipient, direct object or theme, subject or source). 
    
    For synthetic_paraphrase, give an verb that could paraphrase the light verb if is_lvc = TRUE.
    
    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "hacer una pregunta", "hacer ruido")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "hacer calor", "tener miedo")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo", "tomar una decisión")
    - indef_process: complement denotes an ongoing or habitual process with no clear endpoint (e.g., "hacer natación")
    - punctual: complement denotes a single, instantaneous event (e.g., "dar un golpe", "hacer una caricia")    
    - resultative: complement denotes a resulting state, change of state, or outcome (e.g., "dar permiso")
    - incremental: complement denotes a gradual change or accumulation over time (e.g., "dar aumento")
    - causative: subject causes a change in another participant (e.g., "dar miedo a alguien")
    
    Sentence: 
    {text}

    Target verb: {verb_surface}
    The matched_span MUST include the target verb form.

    Left context: {left_context}
    Right context: {right_context}
    Analyze ONLY the verb that fits this context.
    """

def annotate_records(data): 
    '''Calls LLM to annotate each record and returns a list of updated dictionaries; 
    (one dict per record).'''

    # Initialize empty list to hold annotated data 
    model_records = []

    for record in data: 
        #text = record["text"]
        prompt = build_prompt(
            text=record["text"], 
            verb_surface=record["verb_surface"], 
            left_context=record["left_context"], 
            right_context=record["right_context"]
            )
        #print(record) # for debugging

        try: 
            result = call_llm(prompt)
            content = result["choices"][0]["message"]["content"] # model response
            parsed = parse_llm_response(content) # format model response
            #print(content) # for debugging
            
            # Merge LLM annotation with original text 
            updated_record = copy.deepcopy(record)
            updated_record.update(parsed)
            updated_record["id"] = record["id"] 

            # remove trailing and leading whitespace from string values (ignore non-strings)
            updated_record.update({k: v.strip() if isinstance(v, str) else v for k, v in updated_record.items()})

            # Save all changes to return and write to file later
            model_records.append(updated_record)
            print(f"Processed id={record['id']}")

        # Exception / Error Handling... 
        except Exception as e:
            print(f"Error processing id={record.get('id', 'unknown')}: {e}")
    
    return model_records


if __name__ == "__main__": 
    
    # Test on 1 record:
    # record = load_single_record()
    # prompt = build_prompt(record["text"])
    # result = call_llm(prompt)
    # print(json.dumps(result, indent=2, ensure_ascii=False)) 
    # content = result["choices"][0]["message"]["content"]
    # parsed = parse_llm_response(content)
    # print(parsed)

    ##########################
    # Test on bigger dataset

    # To test on partial file: 
    # partial_data = data[110:115] # slice according to datasize
    # annotated_records = annotate_records(partial_data)

    # Load records from interim JSON file
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Run on full file
    annotated_records = annotate_records(data)

    

    # Save annotated output 
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(annotated_records, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(annotated_records)} annotated records to {OUTPUT_FILE}")
    

    