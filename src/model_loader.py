from sentence_transformers import SentenceTransformer

# Smaller and faster than all-MiniLM-L6-v2
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")