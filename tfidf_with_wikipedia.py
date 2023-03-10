#Tf-idf with Wikipedia
'''Now it's your turn to determine new significant terms for your corpus by
applying gensim's tf-idf. You will again have access to the same corpus and
dictionary objects you created in the previous exercises - dictionary, corpus,
and doc. Will tf-idf make for more interesting results on the document level?

TfidfModel has been imported for you from gensim.models.tfidfmodel'''

# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)

#output ->
#[(10, 0.0022676967632877364), (25, 0.004310646654948723),
# (27, 0.008621293309897447),(42, 0.0054444950365925915),
# (43, 0.004310646654948723)]
#reverse 0.4987515710425556
#infringement 0.1854420793422032
#engineering 0.16280628072296138
#interoperability 0.12362805289480211
#reverse-engineered 0.12362805289480211
