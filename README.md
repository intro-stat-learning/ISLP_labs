# ISLP_labs

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/intro-stat-learning/ISLP_labs/v2_devel)


Up-to-date version of labs for ISLP.

This repo will track labs for ISLP as their source code changes.  The
intent is that building a conda environment with
`frozen_requirements.txt` and `torch_requirements.txt` will reproduce
the results in this repo.

Ideally this will be done in a fresh conda environment:

```
conda create -n islp_freeze_311 python=3.11 -y
conda activate islp_freeze_311
```

To install the `v2_devel` version of the requirements run

```
pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v2_devel/frozen_requirements.txt;
pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v2_devel/torch_requirements.txt;.
pip install git+https://github.com/intro-stat-learning/ISLP.git@v2_devel;
```

The labs can now be run from this directory:

```
jupyter lab Ch2-statlearning-lab.ipynb
```

