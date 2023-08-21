FROM docker.io/jupyter/scipy-notebook:lab-4.0.4

# Copy everything from the current directory
# to the Home Directory (/home/jovyan) inside the container
# This will only copy the files that are not ignored by .dockerignore

COPY requirements.txt ${HOME}

# Install the dependencies and remove the requirements file afterwards
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY ./book/docs/labs  ${HOME}/work
