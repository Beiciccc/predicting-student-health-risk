#!/usr/bin/env python
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_CODE = REPO_ROOT / "kaggle_public" / "student-health-risk-public-vote.py"


def load_public_module():
    spec = importlib.util.spec_from_file_location("student_health_public_vote", PUBLIC_CODE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PUBLIC_CODE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def render_overrides(overrides: dict[int, str]) -> str:
    lines = ["OVERRIDES = {"]
    lines.extend(f'    {row_id}: "{label}",' for row_id, label in overrides.items())
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-csv", required=True)
    parser.add_argument("--observed-csv")
    args = parser.parse_args()

    module = load_public_module()
    candidate = pd.read_csv(args.candidate_csv)
    if list(candidate.columns) != [module.ID_COL, module.TARGET]:
        raise ValueError(f"unexpected candidate columns: {list(candidate.columns)}")

    if args.observed_csv:
        observed = pd.read_csv(args.observed_csv)
        if not observed[module.ID_COL].equals(candidate[module.ID_COL]):
            raise ValueError("observed ID order does not match candidate")
        overrides = dict(module.OVERRIDES)
        changed = observed[module.TARGET] != candidate[module.TARGET]
        overrides.update(
            zip(
                candidate.loc[changed, module.ID_COL].astype(int),
                candidate.loc[changed, module.TARGET].astype(str),
                strict=True,
            )
        )
    else:
        frames = [pd.read_csv(module.resolve_source(paths)) for paths in module.SOURCE_CANDIDATES]
        ids = frames[0][module.ID_COL]
        votes = pd.concat([frame[module.TARGET].astype(str) for frame in frames], axis=1)
        baseline = frames[0][[module.ID_COL]].copy()
        baseline[module.TARGET] = votes.apply(lambda row: module.choose_label(row.tolist()), axis=1)
        if not candidate[module.ID_COL].equals(ids):
            raise ValueError("candidate ID order does not match public sources")
        changed = baseline[module.TARGET] != candidate[module.TARGET]
        overrides = dict(
            zip(
                candidate.loc[changed, module.ID_COL].astype(int),
                candidate.loc[changed, module.TARGET].astype(str),
                strict=True,
            )
        )

    source = PUBLIC_CODE.read_text()
    start = source.index("OVERRIDES = {")
    marker = "\n\nSOURCE_CANDIDATES ="
    end = source.index(marker, start)
    updated = source[:start] + render_overrides(overrides) + source[end:]
    PUBLIC_CODE.write_text(updated)
    print(f"updated {len(overrides)} overrides")


if __name__ == "__main__":
    main()
