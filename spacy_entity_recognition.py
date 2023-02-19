'''
Using spaCy's entity recognizer
In this exercise, you'll use spaCy's built-in entity recognizer to
extract names, dates, and organizations from search queries. The spaCy
library has been imported for you, and its English model has been loaded
as nlp.

Your job is to define a function called extract_entities(), which takes
in a single argument message and returns a dictionary with the included
entity types as keys, and the extracted entities as values. The included
entity types are contained in a list called include_entities.

'''
# Define included_entities
include_entities = ['DATE', 'ORG', 'PERSON']

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents

print(extract_entities('friends called Mary who have worked at Google since 2010'))
print(extract_entities('people who graduated from MIT in 1999'))

#OUTPUT
#{'DATE': '2010', 'ORG': None, 'PERSON': None}
#{'DATE': None, 'ORG': None, 'PERSON': None}
