# ISLP_labs

Up-to-date version of labs for ISLP.

This repo will track labs for ISLP as their source code changes.  The
intent is that building a conda environment with
`frozen_requirements.txt` and `torch_requirements.txt` will reproduce
the results in this repo.

To install the `v1` version of the requirements run

```
pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v1/frozen_requirements.txt;
pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v1/torch_requirements.txt;.
pip install ISLP==0.3.17;
```
