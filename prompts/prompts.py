# Prompt 1: includes only boolean LVC yes/no
prompt_one = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - id
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - noun_predicate
    - left_context
    - right_context
    - is_candidate_lvc

    Mark is_candidate_lvc = true when the noun carries the main meaning of the predicate.
    If dar is used to transfer a physical object from a source to a recipient, mark it as false.
    If is_candidate_lvc = false, still return JSON but:
    - noun_predicate = ""

    Sentence: 
    {text}
    """

# Prompt 2: includes 3-way distinction between LVC, borderline, and non-LVC
prompt_two = """You are extracting Spanish light verb constructions. 

    canonical examples: 
    Voy a dar un paseo. → canonical
    Le di un golpe. → canonical
    El libro me da miedo. → canonical

    borderline examples:
    El tema da mucho para discutir. → borderline
    Da para hablar mucho de este punto. → borderline

    non_LVC examples:
    Me dio un libro. → non_lvc
    Le doy el vaso. → non_lvc
    Me daban un dólar por un peso. → non_lvc

    Return JSON only, with no extra text. 
    Fields: 
    - id
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - lvc_type: canonical | borderline | non_lvc
    - confidence_rating: high | medium | low 
    - type_reason

    Mark lvc_type = canonical when the noun carries the main meaning of the predicate.
    Mark lvc_type = borderline when the predicate is non-nominal or idiomatic.
    Mark lvc_type = non_lvc if dar is used to transfer a physical object from a source to a recipient.
    If lvc_type = non_lvc, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain lvc_type in 150 characters or less.

    Sentence: 
    {text}
    """

# Prompt 3: includes reasoning and confidence rating 
prompt_three = """You are extracting Spanish light verb constructions. 

    canonical examples: 
    Voy a dar un paseo. → canonical
    Le di un golpe. → canonical
    El libro me da miedo. → canonical

    borderline examples:
    El tema da mucho para discutir. → borderline
    Da para hablar mucho de este punto. → borderline

    non_LVC examples:
    Me dio un libro. → non_lvc
    Le doy el vaso. → non_lvc
    Me daban un dólar por un peso. → non_lvc

    Return JSON only, with no extra text. 
    Fields: 
    - id
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - lvc_type: canonical | borderline | non_lvc
    - confidence_rating: high | medium | low 
    - type_reason

    Mark lvc_type = canonical when the noun carries the main meaning of the predicate.
    Mark lvc_type = borderline when the predicate is non-nominal or idiomatic.
    Mark lvc_type = non_lvc if dar is used to transfer a physical object from a source to a recipient.
    If lvc_type = non_lvc, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain lvc_type in 150 characters or less.

    Sentence: 
    {text}
    """

# Prompt 4: Changed LVC classification back to T/F and increased its reasoning.
# It generated very short responses
prompt_four = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = TRUE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less.

    Sentence: 
    {text}
    """

# Prompt 5: restricted the model's reason type 
prompt_five = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = TRUE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less. Do not include "main meaning carried by" in your answer.

    Sentence: 
    {text}
    """

# Prompt 6: included Aktionsart 
prompt_six = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - complement_aktionsart: 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = TRUE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less. Do not include "main meaning carried by" in your answer.

    Sentence: 
    {text}
    """

# Removed aktionsarten
prompt_seven = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = TRUE, still return JSON but:
    - verb_predicate = ""
s
    For type_reason, explain why is_lvc in 200 characters or less. 
    Explain which theta roles or meaning conveyed by the complement that causes TRUE or FALSE.

    Sentence: 
    {text}
    """

# Tried to give more explicit instructions about reasoning, and corrected mistake
prompt_eight = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""
s
    For type_reason, explain is_lvc in 200 characters or less. If is_lvc = FALSE, explain recipient, source, and theme. 

    Sentence: 
    {text}
    """

# Tried to add more details about the type of noun 
prompt_nine = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_aspect: stative | process | resultative | punctual | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate.
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less. If is_lvc = FALSE, explain recipient, source, and theme. 
    
    For predicate_aspect, explain the aspectual value of the verb's complement. 
    
    
    Sentence: 
    {text}
    """



# Added more explicit instructions about examples 
prompt_ten = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Positive examples typically can be paraphrased by a synthetic verb.
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Negative examples typically have a an indirect object (recipient), direct object (theme), and subject (source).
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_aspect: stative | process | resultative | punctual | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning of the predicate. 
    Mark is_lvc = FALSE if dar is used to transfer something from a source to a recipient. 
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. If is_lvc = FALSE, explain recipient, source, and theme. 
    
    For predicate_aspect, explain the aspectual value of the verb's complement. 
    
    
    Sentence: 
    {text}
    """

# Fixed a typo 
# Adding more instructions about 
prompt_eleven = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Positive examples typically can be paraphrased by a synthetic verb.
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Negative examples typically have an indirect object (recipient), direct object (theme), and subject (source).
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if dar is used to transfer a physical object from a source to a recipient or if it's a passive participle.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain indirect object or recipient, direct object or theme, and subject or source. 

    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (psychological, emotional, or physiological), with no clear endpoint (e.g., "dar miedo")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
    - indef_process: complement denotes an ongoing or habitual process with no clear endpoint (e.g., "dar apoyo")
    - punctual: complement denotes a single, instantaneous event (e.g., "dar un golpe")    
    - resultative: complement denotes a resulting state, change of state, or outcome (e.g., "dar permiso")
    - incremental: complement denotes a gradual change or accumulation over time (e.g., "dar aumento")
    - causative: subject causes a change in another participant (e.g., "dar miedo a alguien")
    
    
    Sentence: 
    {text}
    """

# Asking for specific complement type, as "predicate_type"
prompt_twelve = """You are extracting Spanish light verb constructions. 

    Positive examples: 
    Positive examples typically can be paraphrased by a synthetic verb.
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Negative examples typically have an indirect object (recipient), direct object (theme), and subject (source).
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if dar is used to transfer a physical object from a source to a recipient or if it's a passive participle.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain indirect object or recipient, direct object or theme, and subject or source. 

    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "dar una respuesta")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "dar miedo")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
    - indef_process: complement denotes an ongoing or habitual process with no clear endpoint (e.g., "dar apoyo")
    - punctual: complement denotes a single, instantaneous event (e.g., "dar un golpe", "darse cuenta")    
    - resultative: complement denotes a resulting state, change of state, or outcome (e.g., "dar permiso")
    - incremental: complement denotes a gradual change or accumulation over time (e.g., "dar aumento")
    - causative: subject causes a change in another participant (e.g., "dar miedo a alguien")
    
    
    Sentence: 
    {text}
    """

# Swapped "Spanish" for "Portuguese" to see if it could generalize immediately to another language
prompt_thirteen ="""You are extracting Portuguese light verb constructions. 

    Positive examples: 
    Positive examples typically can be paraphrased by a synthetic verb.
    Voy a dar un paseo. → TRUE
    Le di un golpe. → TRUE
    El libro me da miedo. → TRUE
    El tema da mucho para discutir. → TRUE
    Da para hablar mucho de este punto. → TRUE

    Negative examples:
    Negative examples typically have an indirect object (recipient), direct object (theme), and subject (source).
    Me dio un libro. → FALSE
    Le doy el vaso. → FALSE
    Me daban un dólar por un peso. → FALSE
    No da nada por la ayuda. → FALSE
    No podían, dado que era gente muy diversa. → FALSE

    Return JSON only, with no extra text. 
    Fields: 
    - text
    - verb_lemma
    - verb_surface
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if dar is used to transfer a physical object from a source to a recipient or if it's a passive participle.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain indirect object or recipient, direct object or theme, and subject or source. 

    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "dar una respuesta")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "dar miedo")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
    - indef_process: complement denotes an ongoing or habitual process with no clear endpoint (e.g., "dar apoyo")
    - punctual: complement denotes a single, instantaneous event (e.g., "dar un golpe", "darse cuenta")    
    - resultative: complement denotes a resulting state, change of state, or outcome (e.g., "dar permiso")
    - incremental: complement denotes a gradual change or accumulation over time (e.g., "dar aumento")
    - causative: subject causes a change in another participant (e.g., "dar miedo a alguien")
    
    
    Sentence: 
    {text}
    """

# Added in some examples with HACER  to see if it could generalize to other constructions
prompt_fourteen = """You are extracting Spanish light verb constructions. 

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
    - matched_span
    - verb_predicate
    - left_context
    - right_context
    - is_lvc: True | False
    - confidence_rating: high | medium | low 
    - type_reason
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if dar is used to transfer a physical object from a source to a recipient or if it's a passive participle.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain indirect object or recipient, direct object or theme, and subject or source. 

    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "hacer una pregunta", "hacer ruido")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "hacer calor")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
    - indef_process: complement denotes an ongoing or habitual process with no clear endpoint (e.g., "hacer natación")
    - punctual: complement denotes a single, instantaneous event (e.g., "dar un golpe", "hacer una caricia")    
    - resultative: complement denotes a resulting state, change of state, or outcome (e.g., "dar permiso")
    - incremental: complement denotes a gradual change or accumulation over time (e.g., "dar aumento")
    - causative: subject causes a change in another participant (e.g., "dar miedo a alguien")
    
    
    Sentence: 
    {text}
    """

# Added LR context and target verb
prompt_fifteen = """You are extracting Spanish light verb constructions. 

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
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if dar is used to transfer a physical object from a source to a recipient or if it's a passive participle.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain indirect object or recipient, direct object or theme, and subject or source. 

    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "hacer una pregunta", "hacer ruido")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "hacer calor")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
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

# forgot to remove DAR from instructions
prompt_sixteen = """You are extracting Spanish light verb constructions. 

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
    - predicate_type: nom | prep | verb | adj
    - predicate_aspect: stative | def_process | indef_process | punctual | resultative | incremental | causative 
    - subject_animacy: animate | inanimate 

    Mark is_lvc = TRUE when the complement of the verb carries the main meaning and the verb does not denote its prototypical meaning.
    Mark is_lvc = FALSE if the verb is used in a way other than its prototypical meaning if the verb_predicate carries more meaning.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""

    For type_reason, explain is_lvc in 200 characters or less, and say which synthetic verb could paraphrase the lvc. 
    If is_lvc = FALSE, explain parts of speech (e.g., indirect object or recipient, direct object or theme, subject or source). 

    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "hacer una pregunta", "hacer ruido")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "hacer calor")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
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

# Made synthetic paraphrase its own field: 
prompt_seventeen = """You are extracting Spanish light verb constructions. 

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
    Mark is_lvc = FALSE if the verb is used in a way other than its prototypical meaning if the verb_predicate carries more meaning.
    If is_lvc = FALSE, still return JSON but:
    - verb_predicate = ""
    - synthetic_paraphrase = ""

    For type_reason, explain is_lvc in 200 characters or less.
    If is_lvc = FALSE, explain parts of speech (e.g., indirect object or recipient, direct object or theme, subject or source). 
    
    For synthetic_paraphrase, give an verb that could paraphrase the light verb if is_lvc = TRUE.
    
    Mark predicate_type based on the category of the predicative element that carries the main semantics:
    - nom: predicative element is a noun (e.g., "hacer una pregunta", "hacer ruido")
    - prep: predicative element is a prepositional phrase (e.g., "No da para tanto.")
    - verb: predicative element is a verb (e.g., "La historia da para escribir un libro.")
    - adj: predicative element is an adjective 
    
    Mark predicate_aspect based on the semantic type of the complement:
    - stative: complement denotes a state (emotional, or physiological), with no clear endpoint (e.g., "hacer calor")
    - def_process: complement denotes a process with a clear endpoint or completion (e.g., "dar un paseo")
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

# minor improvements to prompt
prompt_eighteen = """You are extracting Spanish light verb constructions. 

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
    Negative examples typically have full semantic weight of the verb and parts of speech like subject (agent/source), 
    direct object (theme/patient), indirect object (recipient/beneficiary).
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
    Mark is_lvc = FALSE if the verb_predicate carries more meaning than the verb, and the verb is used in a way other than its prototypical meaning.
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
