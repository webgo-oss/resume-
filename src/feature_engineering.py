CORE_KEYWORDS = [
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "matching",
    "embeddings",
    "vector",
    "semantic search",
    "hybrid search",
    "pinecone",
    "qdrant",
    "milvus",
    "weaviate",
    "faiss",
    "elasticsearch",
    "opensearch",
    "llm",
    "evaluation",
    "ndcg",
    "mrr",
    "map",
    "a/b testing"
]

GOOD_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "applied scientist",
    "search engineer",
    "ranking engineer",
    "recommendation systems engineer",
    "data scientist"
]

AI_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "applied scientist",
    "search engineer",
    "ranking engineer",
    "recommendation engineer",
    "recommendation systems engineer",
    "retrieval engineer",
    "relevance engineer",
    "data scientist",
    "nlp engineer",
    "backend engineer",
    "software engineer"
]

BAD_TITLES = [
    "marketing manager",
    "hr manager",
    "sales manager",
    "recruiter"
]

AI_TITLE_KEYWORDS = [
    "recommendation systems engineer",
    "recommendation engineer",
    "ranking engineer",
    "search engineer",
    "retrieval engineer",
    "relevance engineer",
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "applied scientist",
    "data scientist",
    "nlp engineer",
    "software engineer",
    "backend engineer",
]


def extract_features(candidate):
    features = {}

    profile = candidate["profile"]

    exp = profile["years_of_experience"]

    if 5 <= exp <= 9:
        experience_score = 1.0
    elif 3 <= exp < 5:
        experience_score = 0.7
    elif 9 < exp <= 12:
        experience_score = 0.8
    else:
        experience_score = 0.3

    features["experience_score"] = experience_score

    skill_names = [skill["name"].lower() for skill in candidate["skills"]]

    matches = 0
    for keyword in CORE_KEYWORDS:
        for skill in skill_names:
            if keyword in skill:
                matches += 1
                break

    skill_score = matches / len(CORE_KEYWORDS)
    features["skill_score"] = skill_score
    title = profile["current_title"].lower()

    title_score = 0.5

    for good in GOOD_TITLES:
        if good in title:
            title_score = 1.0
            break

    for bad in BAD_TITLES:
        if bad in title:
            title_score = 0.0
            break

    features["title_score"] = title_score

    title_relevance = 0.0

    for keyword in AI_TITLE_KEYWORDS:
        if keyword in title:
            title_relevance = 1.0
            break

    features["title_relevance"] = title_relevance

    career_text = ""
    for job in candidate["career_history"]:
        career_text += " "
        career_text += job["title"]
        career_text += " "
        career_text += job["description"]

    career_text = career_text.lower()

    career_hits = 0
    for keyword in CORE_KEYWORDS:
        if keyword in career_text:
            career_hits += 1

    career_score = career_hits / len(CORE_KEYWORDS)
    features["career_score"] = career_score

    signals = candidate["redrob_signals"]

    behavior_score = 0.0

    if signals["open_to_work_flag"]:
        behavior_score += 0.2

    behavior_score += signals["recruiter_response_rate"] * 0.2

    github_score = max(0, min(signals["github_activity_score"], 100))
    behavior_score += (github_score / 100) * 0.2

    behavior_score += (
        min(signals["profile_completeness_score"], 100) / 100
    ) * 0.2

    behavior_score += signals["interview_completion_rate"] * 0.2

    features["behavior_score"] = behavior_score

    return features