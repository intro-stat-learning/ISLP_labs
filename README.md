# ISLP_labs

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/intro-stat-learning/ISLP_Labs)

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Authors

- Trevor Hastie

- Gareth James

- Jonathan Taylor

- Robert Tibshirani

- Daniela Witten

### ISLP

Please ensure you have followed the installation instructions for
[ISLP](https://github.com/intro-stat-learning/ISLP). This will address
installation of [jupyterlab](https://github.com/jupyterlab/jupyterlab)
if necessary, which is not included as a requirement of the labs.

### Up-to-date version of labs for ISLP. 

This repo will track labs for ISLP as their source code changes.  The
intent is that building a virtual environment with
`requirements.txt` will reproduce the results in this repo.

To install the current version of the requirements run

```
uv pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v2.2.2/requirements.txt;
```

The labs can now be run via:

```
uv run jupyter lab Ch02-statlearn-lab.ipynb
```


# Zip / tarball

You can download all the labs as a `.zip` or `.tar.gz` [here](https://github.com/intro-stat-learning/ISLP_labs/releases/tag/v2.2.2)

# Setup script

We've added a setup script that ensures precisely the desired labs are checked out along with a `uv` virtual environment being created. Follow
these instructions:

To set up a local environment to run the notebooks for a specific version of the labs, you can use the `setup_notebook_env.py` script. This script will create a directory, download the labs, and set up a Python virtual environment with all the necessary packages.

## Prerequisites

This script relies on `uv` for managing Python environments. If you don't have `uv` installed, you can install it using `pipx` or `cargo`:

*   **Using `pipx` (recommended):**
    ```bash
    pip install pipx
    pipx ensurepath
    pipx install uv
    ```

*   **Using `cargo` (if you have Rust installed):**
    ```bash
    cargo install uv
    ```

For more detailed installation instructions, please refer to the [uv documentation](https://github.com/astral-sh/uv#installation).

## Instructions

### 1. Download the setup script

You can find the raw Python script here: [`setup_notebook_env.py`](https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/main/setup_notebook_env.py)

To download and run it, first ensure `uv` is installed (see Prerequisites above), then execute the following commands in your terminal:

```bash
curl -LO https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/main/setup_notebook_env.py
uv run python setup_notebook_env.py --outdir ISLP_v2.2.2 --commit v2.2.2 --python-version 3.12
```

### 2. Run the setup script

Open your terminal and run the following command to set up the environment for version `v2.2.2` of the labs with Python `3.12`. You can also specify one or more notebooks to run automatically after setup.

*   `--outdir ISLP_v2.2.2`: This will create a directory named `ISLP_v2.2.2` for your labs.
*   `--commit v2.2.2`: This specifies that you want to use version `v2.2.2` of the labs.
*   `--python-version 3.12`: This will use Python 3.12 for the environment.
*   `Ch02-statlearn-lab.ipynb`: This is an optional argument to run a specific notebook after the setup is complete. It is meant for testing to be sure given notebooks run but is not required. You can list more than one notebook.

### 2. Activate the environment

Once the script is finished, you can activate the virtual environment to run other notebooks or work with the lab materials.

*   **On macOS and Linux:**
    ```bash
    source ISLP_v2.2.2/.venv/bin/activate
    ```

*   **On Windows:**
    ```bash
    ISLP_v2.2.2\.venv\Scripts\activate
    ```

### 3. Run other notebooks

After activating the environment, you can start Jupyter Lab to run other notebooks.

```bash
jupyter lab
```


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tibshirani"><img src="https://avatars.githubusercontent.com/u/2848609?v=4?s=100" width="100px;" alt="tibshirani"/><br /><sub><b>tibshirani</b></sub></a><br /><a href="https://github.com/intro-stat-learning/ISLP_labs/commits?author=tibshirani" title="Code">💻</a> <a href="#content-tibshirani" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://web.stanford.edu/~hastie/"><img src="https://avatars.githubusercontent.com/u/13293253?v=4?s=100" width="100px;" alt="trevorhastie"/><br /><sub><b>trevorhastie</b></sub></a><br /><a href="https://github.com/intro-stat-learning/ISLP_labs/commits?author=trevorhastie" title="Code">💻</a> <a href="#content-trevorhastie" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/danielawitten"><img src="https://avatars.githubusercontent.com/u/12654191?v=4?s=100" width="100px;" alt="danielawitten"/><br /><sub><b>danielawitten</b></sub></a><br /><a href="https://github.com/intro-stat-learning/ISLP_labs/commits?author=danielawitten" title="Code">💻</a> <a href="#content-danielawitten" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tschm"><img src="https://avatars.githubusercontent.com/u/2046079?v=4?s=100" width="100px;" alt="Thomas Schmelzer"/><br /><sub><b>Thomas Schmelzer</b></sub></a><br /><a href="https://github.com/intro-stat-learning/ISLP_labs/commits?author=tschm" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://statweb.stanford.edu/~jtaylo"><img src="https://avatars.githubusercontent.com/u/341611?v=4?s=100" width="100px;" alt="Jonathan Taylor"/><br /><sub><b>Jonathan Taylor</b></sub></a><br /><a href="https://github.com/intro-stat-learning/ISLP_labs/commits?author=jonathan-taylor" title="Code">💻</a> <a href="#content-jonathan-taylor" title="Content">🖋</a></td>
</tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
