'''
Rasa NLU
In this exercise, you'll use Rasa NLU to create an interpreter,
which parses incoming user messages and returns a set of entities.
Your job is to train an interpreter using the MITIE entity recognition
model in Rasa NLU.

'''


# Import necessary modules
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

# Create args dictionary
args = {"pipeline":"spacy_sklearn"}

# Create a configuration and trainer
config = RasaNLUConfig(cmdline_args=args)
trainer = Trainer(config)

# Load the training data
training_data = load_data("./training_data.json")

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

# Test the interpreter
print(interpreter.parse("I'm looking for a Mexican restaurant in the North of town"))

#OUTPUT
'''
Fitting 2 folds for each of 6 candidates, totalling 12 fits
{'intent': {'name': 'restaurant_search', 'confidence': 0.6627604390878398},
'entities': [{'start': 18, 'end': 25, 'value': 'mexican', 'entity': 'cuisine',
'extractor': 'ner_crf'}, {'start': 44, 'end': 49, 'value': 'north',
'entity': 'location', 'extractor': 'ner_crf'}],
'intent_ranking': [{'name': 'restaurant_search',
'confidence': 0.6627604390878398}, {'name': 'goodbye',
'confidence': 0.14633725788681204}, {'name': 'affirm',
'confidence': 0.09756426473688806}, {'name': 'greet',
'confidence': 0.09333803828846025}], 'text': "I'm looking for
a Mexican restaurant in the North of town"}


'''
