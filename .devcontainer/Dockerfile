FROM python:3.12-slim

## Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy UV installer
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

RUN uv pip install --system --no-cache-dir jupyter ipykernel

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir -p /workspace \
    && chown -R $USERNAME:$USERNAME /workspace

# Configure Jupyter
# USER $USERNAME
WORKDIR /workspace

RUN jupyter notebook --generate-config \
    && echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py \
    && echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py \
    && echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py



# Install and configure jupyter
#RUN jupyter notebook --generate-config && \
#    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
#    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Set up health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8888 || exit 1

# Set up entrypoint
EXPOSE 8888
CMD ["uv", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]


