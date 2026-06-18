def build_candidate_text(candidate):
    profile = candidate["profile"]

    parts = [
        profile["headline"],
        profile["current_title"],
    ]
    for skill in candidate["skills"][:15]:
        parts.append(skill["name"])
    for job in candidate["career_history"][:3]:
        parts.append(job["title"])
        parts.append(job["description"][:200])

    return " ".join(parts)


def build_career_text(candidate):
    parts = []
    for job in candidate["career_history"][:3]:
        parts.append(job["title"])
        parts.append(job["description"][:200])

    return " ".join(parts)