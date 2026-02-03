.DEFAULT_GOAL := help

PYTHON_VERSION := $(shell cat .python-version)

venv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv --python $(PYTHON_VERSION)

.PHONY: install
install: venv ## Install all dependencies (in the virtual environment) defined in requirements.txt
	@uv pip install --upgrade pip
	@uv pip install -r requirements.txt


.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort


.PHONY: jupyter
jupyter: install  ## Install and start jupyter Lab
	@uv run pip install jupyterlab
	@uv run jupyter lab


.PHONY: marimo
marimo: install ## Install and start marimo
	@uv run pip install marimo
	@uv run marimo edit --no-token --headless .
