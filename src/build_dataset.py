'''This script loads data, filters for the target verb, 
and saves the matches to a structured JSON output'''

import json
import load_data
from config import CORPUS_FILE, TARGET_VERBS

#### CONFIGS #### 
corpus_file = CORPUS_FILE


def format_data(records, language="es"): 
    '''Takes list of dicts (one per sentence in records) and returns a new record with
      id and language for each record'''

    # Initialize empty list to hold sentence dicts
    new_records = []

    # Create new dict for each sentence in filtered data 
    for i, record in enumerate(records): 
        new_record = {
            "id": i + 1, 
            "language": language, 
            **record
        }
        
        new_records.append(new_record)

    return new_records

if __name__ == "__main__": 

    # load data and filter data
    data = load_data.load_corpus()
    records = load_data.filter_data(data, max_matches=25)

    # Create structured dictionary format 
    structured_data = format_data(records, language="es")
    #print(structured_data)

    # save to JSON format 
    file_name = "verb_candidates.json"
    with open(f"data/interim/{file_name}", "w", encoding="utf-8") as outfile:
        json.dump(structured_data, outfile, indent=2)

