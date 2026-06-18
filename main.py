from src.load_data import load_candidates, load_jd
from src.ranker import rank_candidates
from src.export_results import export_results

candidates = load_candidates("data/candidates.jsonl")
jd = load_jd("data/job_description.txt")

results = rank_candidates(
    candidates,
    jd,
    batch_size=128
)

export_results(results, "submission.csv")

print("Submission file generated!")