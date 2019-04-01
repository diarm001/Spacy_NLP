import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load("en_core_web_sm")

txt = open('test.txt').read()

doc = nlp(txt)

#Analyse Syntax 

#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

#print("Adverbs:", [token.lemma_ for token in doc if token.pos_ == "ADV"])

# Find named entities, phrases and concepts

#for entity in doc.ents:
 #   print(entity.text, entity.label_)



# Heads and children relations in a dependency tree

#for token in doc:
#    print(token.text, token.dep_, token.head.text, token.head.pos_,
#            [child for child in token.children])

verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)