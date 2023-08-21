FROM docker.io/jupyter/base-notebook:lab-4.0.5

COPY requirements.txt .

# Install Python deps, the user approach is documented here:
# https://pythonspeed.com/articles/multi-stage-docker-python/
RUN pip install --user --no-cache-dir -r requirements.txt

COPY --chown=jovyan:users . ${HOME}/work


