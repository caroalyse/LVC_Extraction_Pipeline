zero_shot = """You are extracting Spanish light verb constructions. 

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

   Sentence: 
   {text}
   """