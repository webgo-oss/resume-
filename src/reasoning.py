def generate_reasoning(
    candidate,
    features,
    semantic_score,
    final_score
):
    profile = candidate["profile"]

    title = profile["current_title"]
    experience = profile["years_of_experience"]

    reasoning = (
        f"{title} with "
        f"{experience:.1f} years experience; "
        f"title relevance {features['title_relevance']:.2f}; "
        f"skill score {features['skill_score']:.2f}; "
        f"career score {features['career_score']:.2f}; "
        f"behavior score {features['behavior_score']:.2f}; "
        f"semantic score {semantic_score:.2f}; "
        f"final score {final_score:.2f}"
    )

    return reasoning