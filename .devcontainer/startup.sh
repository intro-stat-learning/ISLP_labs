#!/bin/bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
uv pip install --no-cache-dir jupyter notebook
uv pip install --no-cache-dir -r requirements.txt