import json

# Load catalog
with open("data/catalog.json", "r") as f:
    catalog = json.load(f)

def search_assessments(query, top_k=5):

    query = query.lower()

    results = []

    for item in catalog:

        text = (
            item.get("name", "") + " " +
            item.get("description", "") + " " +
            item.get("test_type", "")
        ).lower()

        if any(word in text for word in query.split()):

            results.append(item)

    # fallback
    if not results:
        results = catalog[:top_k]

    return results[:top_k]