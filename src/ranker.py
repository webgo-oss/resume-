from tqdm import tqdm

from src.feature_engineering import extract_features
from src.candidate_text import build_candidate_text, build_career_text
from src.semantic_ranker import set_jd_embedding, semantic_scores
from src.career_match import career_semantic_scores
from src.scorer import calculate_final_score
from src.reasoning import generate_reasoning


def rank_candidates(candidates, jd_text, batch_size=128):
    if not candidates:
        return []

    set_jd_embedding(jd_text)

    features_list = []
    candidate_texts = []
    career_texts = []

    for candidate in tqdm(candidates, desc="Preparing texts/features"):
        features_list.append(extract_features(candidate))
        candidate_texts.append(build_candidate_text(candidate))
        career_texts.append(build_career_text(candidate))

    sem_scores = semantic_scores(candidate_texts, batch_size=batch_size)
    career_scores = career_semantic_scores(career_texts, batch_size=batch_size)

    results = []

    for candidate, features, sem_score, career_sem_score in tqdm(
        zip(candidates, features_list, sem_scores, career_scores),
        total=len(candidates),
        desc="Scoring"
    ):
        sem_score = float(sem_score)
        career_sem_score = float(career_sem_score)

        final_score = calculate_final_score(
            features,
            sem_score,
            career_sem_score
        )

        reasoning = generate_reasoning(
            candidate,
            features,
            sem_score,
            final_score
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": final_score,
            "reasoning": reasoning
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results