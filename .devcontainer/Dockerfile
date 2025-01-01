FROM jupyter/base-notebook:latest

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# copy /uv folder into /bin
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /workspace

USER $NB_UID
EXPOSE 8888

#FROM python:3.12-slim

## Install build dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    git \
#    curl \
#    && rm -rf /var/lib/apt/lists/*

# Copy UV installer
#COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#WORKDIR /workspace

#RUN #uv venv /workspace/.venv && \
#RUN uv pip install --system --no-cache-dir jupyter ipykernel


# Create a non-root user
#ARG USERNAME=vscode
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID

#RUN groupadd --gid $USER_GID $USERNAME \
#    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Setup default python tools in a venv
#ENV PATH="/workspace/.venv/bin:$PATH"

# Install and configure jupyter
#RUN jupyter notebook --generate-config
#RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py
#RUN echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Set up entrypoint
#EXPOSE 8888
#CMD ["uv", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


