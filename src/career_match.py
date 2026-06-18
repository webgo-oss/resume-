from src.model_loader import model

CAREER_QUERY = """
Built search systems,
recommendation systems,
matching systems,
retrieval systems,
ranking systems,
candidate matching,
marketplace ranking,
semantic search,
production ML systems,
vector databases,
embeddings,
hybrid retrieval,
LLM based ranking.
"""

CAREER_QUERY_EMBEDDING = model.encode(
    CAREER_QUERY,
    convert_to_numpy=True,
    normalize_embeddings=True
)


def career_semantic_scores(career_texts, batch_size=128):
    career_embeddings = model.encode(
        career_texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return career_embeddings @ CAREER_QUERY_EMBEDDING