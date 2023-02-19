#Specify token sequence length with BOW

#using the review column and specify the sequence length of tokens.
from sklearn.feature_extraction.text import CountVectorizer 

# Build the vectorizer, specify token sequence and fit
vect = CountVectorizer(ngram_range=(1, 2))
vect.fit(reviews.review)

# Transform the review column
X_review = vect.transform(reviews.review)

# Create the bow representation
X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
print(X_df.head())

#Output:
'''

   10  10 95  10 cups  100  100 years  ...  zelbessdisk  zelbessdisk three  zen  zen baseball  zen motorcycle
0   0      0        0    0          0  ...            0                  0    0             0               0
1   0      0        0    0          0  ...            0                  0    0             0               0
2   0      0        0    0          0  ...            0                  0    0             0               0
3   0      0        0    0          0  ...            1                  1    0             0               0
4   0      0        0    0          0  ...            0                  0    0             0               0

[5 rows x 8436 columns]
'''
