#Comparing NLTK with spaCy NER
#Using the same text you used in the first exercise of this chapter, you'll now
#see the results using spaCy's NER annotator. How will they compare?

#The article has been pre-loaded as article. To minimize execution times,
#you'll be asked to specify the keyword argument disable=['tagger', 'parser',
#'matcher'] when loading the spaCy model, because you only care about the
#entity in this exercise.


# Import spacy
import spacy
# Instantiate the English model: nlp
nlp = spacy.load('en_core_web_sm')

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_ , ent.text)
#Output->
    '''
ORG Apple
PERSON Travis Kalanick of Uber
PERSON Tim Cook
ORG Apple
CARDINAL Millions
LOC Silicon Valley
ORG Yahoo
PERSON Marissa Mayer
MONEY 186'''
