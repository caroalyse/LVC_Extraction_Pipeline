'''
This script loads and filters data from the specified corpus.
'''

import gzip
import re
import json

from config import CORPUS_FILE, TARGET_VERBS, VERB_LEMMAS 

#### CONFIGS #### 
corpus_file = CORPUS_FILE
LEFT_WINDOW = 2
RIGHT_WINDOW = 2


def load_sample(): 
    texts_v1 = [
        "Esto da miedo.", 
        "Voy a dar un paseo.", 
        "Le di una mirada.",
        "No quiero dar una respuesta todavía.", 
        "Me parece interesante.", 
        "Daniel tiene mucho que decir.", 
        "Debemos trabajar en el proyecto luego.", 
        "Mis estudiantes me mandaron su tarea.", 
        "La comida es de Miguel."
    ]

    texts = [
    # Clear LVCs
    "Voy a dar un paseo después de clase.",
    "Le di una mirada rápida al documento.",
    "No quiero dar una respuesta todavía.",
    "La profesora dio una explicación clara.",
    "Mis padres me dieron permiso para salir.",
    "El comentario me dio vergüenza.",
    "La noticia nos dio alegría.",
    "Te doy las gracias por tu ayuda.",
    "Ellos daban apoyo a los estudiantes.",
    
    # Borderline / interesting cases
    "Esto da miedo.",
    "La película da mucho que pensar.",
    "Ese tema da lugar a muchas discusiones.",
    "El ruido me da dolor de cabeza.",
    "Este asunto da para hablar.",
    
    # Clearly non-LVC (lexical dar)
    "Mi madre me dio un libro ayer.",
    "Le doy el vaso a mi hermano.",
    "Nos dieron comida en el evento.",
    "El maestro dará la hoja a cada alumno.",
    "Dame el cuaderno, por favor.",
    "Le daré el premio al ganador.",
    "Siempre da abrazos cuando llega.", 

    # Non-dar examples 
    "Me parece interesante.", 
    "Daniel tiene mucho que decir.", 
    "Debemos trabajar en el proyecto luego.", 
    "Mis estudiantes me mandaron su tarea.", 
    "La comida es de Miguel."
]

    return texts 

def load_corpus(): 
    '''Opens text data and returns list of sentences as 'text' field.'''

    data = []

    # Select file opener
    opener = gzip.open if corpus_file.endswith(".gz") else open 

    with opener(corpus_file, "rt", encoding="utf-8", errors="ignore") as f: 
        for line in f:
            text = line.strip()
            if not text: 
                continue
            data.append(text)

    print(f"Loaded {len(data)} rows of data from {corpus_file}")
    #print(data[:5])
    print()
    return data


def find_verbs(text, verb_lemmas=VERB_LEMMAS): 
    '''Returns list of matched verb lemmas in the text.
    
    :param text: Text input from corpus. 
    :param verb_lemmas: dict of lemmas mapped from inflections'''

    # Normalize/tokenize text
    words = re.findall(r"\b\w+\b", text.lower())

    matches = []
    for i, word in enumerate(words): 
        if word in verb_lemmas: 
            matches.append({
                "lemma": verb_lemmas[word], 
                "form": word,
                "index": i
            })

    return matches, words


def filter_data(data, target_verbs=TARGET_VERBS, max_matches=5): 
    '''Returns a dict of (verb_lemma: sentences) that contain the target verb(s).
    
    :param data: text data
    :param target_verbs: list of verbs to match in text data'''

    records = []
    verb_cts = {verb: 0 for verb in target_verbs}

    # Keep track of all matches
    match_ct = 0

    for text in data: 
        matches, words = find_verbs(text)
        
        for match in matches: 
            lemma = match["lemma"]

            if lemma not in target_verbs:
                continue

            if verb_cts[lemma] >= max_matches: 
                continue

            i = match["index"]

            left_context = words[max(0, i - LEFT_WINDOW):i]
            right_context = words[i+1:i+1+RIGHT_WINDOW]

            record = {
                "text": text, 
                "verb_lemma": lemma, 
                "verb_surface": match["form"], 
                "left_context": " ".join(left_context), 
                "right_context": " ".join(right_context)
            }

            records.append(record)
            verb_cts[lemma] += 1
            match_ct += 1

        if all(verb_cts[verb] >= max_matches for verb in target_verbs): 
            break

    print(f"Found {match_ct} matches\n")
    return records



    