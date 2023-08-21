FROM docker.io/jupyter/minimal-notebook:lab-4.0.5 as build

# Copy everything from the current directory
# to the Home Directory (/home/jovyan) inside the container
# This will only copy the files that are not ignored by .dockerignore

COPY requirements.txt ${HOME}

# Setup the virtualenv
RUN python -m venv ${HOME}/venv

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt


FROM docker.io/jupyter/base-notebook:lab-4.0.5 as main
COPY --from=build /home/jovyan/venv ${HOME}/venv
COPY . ${HOME}
