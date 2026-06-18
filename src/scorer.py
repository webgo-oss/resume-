def calculate_final_score(
    features,
    semantic_score,
    career_semantic_score
):
    score = (
        0.20 * features["career_score"] +
        0.15 * career_semantic_score +
        0.20 * features["behavior_score"] +
        0.15 * features["title_score"] +
        0.10 * features["skill_score"] +
        0.10 * features["experience_score"] +
        0.10 * semantic_score
    )

    if features["title_relevance"] == 0:
        score *= 0.50

    eligibility = features["career_score"] + career_semantic_score
    if eligibility < 0.15:
        score *= 0.40

    return score