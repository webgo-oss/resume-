from src.model_loader import model

JD_EMBEDDING = None


def set_jd_embedding(jd_text):
    global JD_EMBEDDING
    JD_EMBEDDING = model.encode(
        jd_text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def semantic_scores(candidate_texts, batch_size=128):
    if JD_EMBEDDING is None:
        raise ValueError("JD embedding is not set. Call set_jd_embedding(jd_text) first.")

    candidate_embeddings = model.encode(
        candidate_texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return candidate_embeddings @ JD_EMBEDDING