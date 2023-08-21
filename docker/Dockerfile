FROM docker.io/jupyter/minimal-notebook:lab-4.0.5

# Copy everything from the current directory
# to the Home Directory (/home/jovyan) inside the container
# This will only copy the files that are not ignored by .dockerignore

COPY . ${HOME}

# Install the dependencies and remove the requirements file afterwards
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
