'''
Store corpus and verb information here to keep script files clean and to expand scope.
'''

# Corpus
CORPUS_FILE = 'name-of-corpus-file'

# Target Verbs
TARGET_VERBS = ["dar", "hacer", "tomar", "tener"]

# Verb inflections
# for naive text matching, gets tokenized 

VERB_FORMS = {
    "dar": """doy, das, da, damos, dais, dan,
              di, diste, dio, dimos, disteis, dieron,
              daba, dabas, dábamos, dabais, daban,
              daré, darás, dará, daremos, daréis, darán,
              daría, darías, daríamos, daríais, darían,
              dé, des, demos, deis, den,
              diera, dieras, diéramos, dieran,
              dado, dar, dando""", 

    "hacer": """hago, haces, hace, hacemos, hacéis, hacen,
            hice, hiciste, hizo, hicimos, hicisteis, hicieron,
            hacía, hacías, hacíamos, hacíais, hacían,
            haré, harás, hará, haremos, haréis, harán,
            haría, harías, haríamos, haríais, harían,
            haga, hagas, hagamos, hagáis, hagan,
            hiciera, hicieras, hiciéramos, hicieran,
            hecho, hacer, haciendo""", 

    "tomar": """tomo, tomas, toma, tomamos, tomáis, toman,
            tomé, tomaste, tomó, tomamos, tomasteis, tomaron,
            tomaba, tomabas, tomábamos, tomabais, tomaban,
            tomaré, tomarás, tomará, tomaremos, tomaréis, tomarán,
            tomaría, tomarías, tomaríamos, tomaríais, tomarían,
            tome, tomes, tomemos, toméis, tomen,
            tomara, tomaras, tomáramos, tomaran,
            tomado, tomar, tomando""", 

    "tener": """tengo, tienes, tiene, tenemos, tenéis, tienen,
            tuve, tuviste, tuvo, tuvimos, tuvisteis, tuvieron,
            tenía, tenías, teníamos, teníais, tenían,
            tendré, tendrás, tendrá, tendremos, tendréis, tendrán,
            tendría, tendrías, tendríamos, tendríais, tendrían,
            tenga, tengas, tengamos, tengáis, tengan,
            tuviera, tuvieras, tuviéramos, tuvieran,
            tenido, tener, teniendo"""
    
}

#### portuguese ##### 
# VERB_FORMS = {
#     "dar": """dou, dás, dá, damos, dais, dão,
#             dei, deste, deu, demos, destes, deram,
#             dava, davas, dávamos, dávais, davam,
#             darei, darás, dará, daremos, dareis, darão,
#             daria, darias, daríamos, daríeis, dariam,
#             dê, dês, demos, deis, deem,
#             desse, desses, déssemos, dessem,
#             der, deres, dermos, derdes, derem,
#             dar, dares, dar, darmos, dardes, darem,
#             dado, dar, dando"""
# }


# Map inflections to joint set 
def build_verb_set(target_verbs, verb_forms_dict): 
    '''Takes list of verbs and their corresponding dicts and outputs a set of all verb inflections'''
    all_verb_forms = []
    for verb in target_verbs: 
        forms_str = verb_forms_dict.get(verb, "") # get long text str of verbs
        forms = [f.strip().lower() for f in forms_str.split(",") if f.strip()] # get each verb from inflection list
        all_verb_forms.extend(forms)
    return set(all_verb_forms)

FORMS_SET = build_verb_set(TARGET_VERBS, VERB_FORMS)

# Map inflections to lemmas 
def build_lemmas(verb_forms_dict): 
    lemma_map = {}
    for lemma, forms_str in verb_forms_dict.items():
        forms = [f.strip().lower() for f in forms_str.split(",") if f.strip()]
        for form in forms: 
            lemma_map[form] = lemma

    return lemma_map

VERB_LEMMAS = build_lemmas(VERB_FORMS)
