import json


def save_results(candidates, job, filename="results.json"):
    data = {"job": job, "candidates": [c.to_dict() for c in candidates]}
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)