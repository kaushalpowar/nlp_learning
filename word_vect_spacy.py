#word vectors with spaCy
'''
In this exercise you'll get your first experience with word vectors!

You're going to use the ATIS dataset, which contains thousands of sentences
from real people interacting with a flight booking system.

The user utterances are available in the list sentences, and the corresponding
intents in labels.

Your job is to create a 2D array X with as many rows as there are sentences in
the dataset, where each row is a vector describing that sentence.

'''
# Load the spacy model: nlp
nlp = spacy.load('en')

# Calculate the length of sentences
n_sentences = len(sentences)

# Calculate the dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros: X
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
for idx, sentence in enumerate(sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(sentence)
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector
