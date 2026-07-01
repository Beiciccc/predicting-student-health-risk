#!/usr/bin/env bash
set -euo pipefail

mkdir -p input
kaggle competitions download -c playground-series-s6e7 -p input --force
unzip -o input/playground-series-s6e7.zip -d input
