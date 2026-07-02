#!/usr/bin/env python
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


FIELDS = [
    "submitted_at_utc",
    "submission_ref",
    "name",
    "public_score",
    "local_cv",
    "beta",
    "method",
    "notes",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    lines = [
        "# Results Summary",
        "",
        "Balanced accuracy is the competition metric. Local CV is computed from out-of-fold predictions.",
        "",
        "| # | Submitted (UTC) | Ref | Name | Public score | Local CV | Beta | Method | Notes |",
        "|---:|---|---|---|---:|---:|---:|---|---|",
    ]
    for i, row in enumerate(rows, start=1):
        lines.append(
            "| {i} | {submitted_at_utc} | {submission_ref} | {name} | {public_score} | {local_cv} | {beta} | {method} | {notes} |".format(
                i=i,
                submitted_at_utc=row.get("submitted_at_utc", ""),
                submission_ref=row.get("submission_ref", ""),
                name=row.get("name", ""),
                public_score=row.get("public_score", ""),
                local_cv=row.get("local_cv", ""),
                beta=row.get("beta", ""),
                method=row.get("method", ""),
                notes=row.get("notes", ""),
            )
        )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-json", required=True)
    parser.add_argument("--submission-ref", required=True)
    parser.add_argument("--public-score", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--notes", default="")
    parser.add_argument("--csv", default="reports/submissions.csv")
    parser.add_argument("--markdown", default="reports/results_summary.md")
    args = parser.parse_args()

    candidate = json.loads(Path(args.candidate_json).read_text())
    local_cv = candidate.get("oof_balanced_accuracy", "")
    if local_cv in ("", None):
        local_cv_text = ""
    else:
        local_cv_text = f"{float(local_cv):.6f}"
    beta = candidate.get("beta", "")
    if beta in ("", None):
        beta_text = ""
    else:
        beta_text = f"{float(beta):.4f}"

    row = {
        "submitted_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "submission_ref": args.submission_ref,
        "name": candidate.get("name", ""),
        "public_score": args.public_score,
        "local_cv": local_cv_text,
        "beta": beta_text,
        "method": args.method,
        "notes": args.notes,
    }
    csv_path = Path(args.csv)
    rows = read_rows(csv_path)
    rows.append(row)
    write_rows(csv_path, rows)
    write_markdown(Path(args.markdown), rows)
    print(json.dumps(row, indent=2))


if __name__ == "__main__":
    main()
