import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load catalog
with open("data/catalog.json", "r") as f:
    catalog = json.load(f)

# Extract descriptions
texts = [
    item.get("description", "")
    for item in catalog
]

# Remove empty descriptions
texts = [text for text in texts if text.strip()]

# Generate embeddings
embeddings = model.encode(texts)

# Convert to numpy array
embeddings = np.array(embeddings)

# Handle single embedding case
if len(embeddings.shape) == 1:
    embeddings = embeddings.reshape(1, -1)

dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

def search_assessments(query, top_k=5):

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(catalog):
            results.append(catalog[idx])

    return results