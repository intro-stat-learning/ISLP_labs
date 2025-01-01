FROM python:3.12-slim

# Install system dependencies
#RUN apt-get update && apt-get install -y \
#    git \
#    curl \
#    && rm -rf /var/lib/apt/lists/*

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy UV installer
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

COPY requirements.txt ./

RUN uv venv /workspace/.venv && \
    uv pip install --no-cache-dir jupyter && \
    uv pip install --no-cache-dir -r requirements.txt \

# Install Jupyter and common data science packages
#RUN pip3 install --no-cache-dir \
#    jupyter

# Set up working directory
# WORKDIR /workspace

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Setup default python tools in a venv
#RUN python -m venv /opt/venv
ENV PATH="/workspace/.venv/bin:$PATH"

# Install and configure jupyter
RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Set up entrypoint
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]