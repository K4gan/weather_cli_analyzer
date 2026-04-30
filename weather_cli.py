from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def summarize(rows: list[dict[str, str]]) -> dict[str, dict[str, float]]:
    buckets: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        buckets[row["city"]].append(float(row["temp_c"]))
    return {
        city: {"days": len(values), "avg_temp_c": sum(values) / len(values), "max_temp_c": max(values)}
        for city, values in buckets.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize weather CSV files by city.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    for city, stats in summarize(load_rows(args.csv_path)).items():
        print(f"{city}: days={stats['days']} avg={stats['avg_temp_c']:.1f}C max={stats['max_temp_c']:.1f}C")


if __name__ == "__main__":
    main()
