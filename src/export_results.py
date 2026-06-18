import csv


def export_results(results, output_file):
    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.writer(f)

        writer.writerow([
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ])

        for rank, candidate in enumerate(results, start=1):
            writer.writerow([
                candidate["candidate_id"],
                rank,
                round(candidate["score"], 4),
                candidate["reasoning"]
            ])