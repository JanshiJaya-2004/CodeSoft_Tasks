from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Sample movie dataset
df = pd.DataFrame({
    'Movie': ['A', 'B', 'C'],
    'Description': ['action adventure', 'romance drama', 'action thriller']
})

# Vectorize the descriptions
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(df['Description'])

# Compute cosine similarity
similarity_matrix = cosine_similarity(vectors)

# Print the full similarity matrix
print("Cosine Similarity Matrix:")
print(pd.DataFrame(similarity_matrix, index=df['Movie'], columns=df['Movie']))

# Print specific similarities
print("\nSimilarity between Movie A and B:", similarity_matrix[0][1])
print("Similarity between Movie A and C:", similarity_matrix[0][2])
