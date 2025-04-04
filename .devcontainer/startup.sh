#!/bin/bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12
uv pip install --no-cache-dir jupyterlab
uv pip install --no-cache-dir -r requirements.txt
