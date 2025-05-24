# Set the default target to help
.DEFAULT_GOAL := help

# Development Setup
venv: ## Create a Python virtual environment using uv
	@curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv package manager
	@uv venv --python 3.12  # Create a virtual environment with Python 3.12


# Declare install as a phony target (not a file)
.PHONY: install
install: venv ## Install all dependencies (in the virtual environment) defined in requirements.txt
	@uv pip install --upgrade pip  # Ensure pip is up to date
	@uv pip install -r requirements.txt  # Install dependencies from requirements.txt


# Declare help as a phony target
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"  # Print header in bold
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort  # Extract and format targets with comments


# Jupyter Setup
.PHONY: jupyter
jupyter: install  ## Install and start jupyter Lab
	@uv run pip install jupyterlab  # Install JupyterLab
	@uv run jupyter lab  # Start JupyterLab server
