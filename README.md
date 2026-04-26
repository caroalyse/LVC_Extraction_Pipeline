# Final Project: LVC Extraction Pipeline (Spanish/Portuguese)

This project builds a small LLM-assisted pipeline for identifying and analyzing **light verb constructions (LVCs)** using a combination of rule-based filtering and LLM-based annotation from corpus data. 

## Overview

Light verb constructions (e.g., *dar un paseo*, *hacer una pregunta*) are challenging to detect because meaning is distributed between the verb and its complement. This project explores a hybrid approach:

1. **Rule-based candidate extraction**
2. **Structured data transformation**
3. **LLM-assisted semantic annotation**

The result is a structured dataset enriched with linguistic features such as predicate type, aspect, and animacy.

---

## Pipeline

The pipeline follows an ETL-style architecture:

```
Raw Corpus Data
    ↓
load_corpus()
    ↓
filter_data()  → candidate verb instances
    ↓
format_data()  → add metadata (id, language)
    ↓
LLM annotation → semantic analysis and annotation
    ↓
Final JSON dataset
```

---

## Project Structure

```
.
├── src/                # Core pipeline scripts
├── prompts/            # Prompt templates for LLM annotation
├── data/
│   ├── interim/        # Candidate verb matches
│   └── processed/      # Annotated output
├── .env.example        # Environment variable template
├── .gitignore
├── README.md
├── requirements.txt
```

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/caroalyse/LVC_Extraction_Pipeline.git
cd LVC_Extraction_Pipeline
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file based on `.env.example`:

```
API_KEY=your_api_key_here
LLM_API_URL=your_endpoint
LLM_MODEL=your_model_name
```

---

## Usage

### Step 1: Extract candidate verbs

```
python src/build_dataset.py
```

Output:

```
data/interim/verb_candidates.json
```

---

### Step 2: Annotate with LLM

```
python src/annotate_records.py
```

Output:

```
data/processed/verbs_annotated.json
```

Sample of Output: 
```json
{
    "id": 1,
    "language": "es",
    "text": "Si partimos de esa noción y seguimos desde ahí, podemos dar el siguiente paso, que es que si el océano no está contento, nadie lo está.",
    "verb_lemma": "dar",
    "verb_surface": "dar",
    "left_context": "ahí podemos",
    "right_context": "el siguiente",
    "matched_span": "dar el siguiente paso",
    "verb_predicate": "el siguiente paso",
    "is_lvc": true,
    "confidence_rating": "high",
    "type_reason": "The verb 'dar' loses its prototypical meaning of giving/transferring and functions as a light verb for the noun 'paso'.",
    "synthetic_paraphrase": "avanzar",
    "predicate_type": "nom",
    "predicate_aspect": "def_process",
    "subject_animacy": "animate"
  }
```
---

## Output Format

Each record contains:

* text
* verb_lemma
* verb_surface
* context (left/right)
* is_lvc (True/False)
* predicate_type
* predicate_aspect
* subject_animacy
* confidence_rating
* type_reason
* synthetic_paraphrase


---

## Motivation

This project addresses a key challenge in descriptive and computational linguistics:

> LVCs are difficult to identify due to semantic ambiguity and gradient classification.
> LVCs raise interesting questions about language change, such as verb auxiliarization. 

By combining rule-based filtering with LLM-based annotation, this pipeline explores a scalable approach to semantic classification in corpus data.

---

## Future Work

* Improve LLM classification accuracy
* Model predicate relationships
* Scale to larger, messier corpora (e.g., Reddit dumps)
* Evaluate against annotated linguistic datasets

---

## Tech Stack

* Python
* JSON-based data modeling
* LLM API (e.g., Gemma / LLaMA)
* Regex-based text processing

---

## Notes

* API keys are not included in this repository.
* Use `.env` to configure credentials securely.
