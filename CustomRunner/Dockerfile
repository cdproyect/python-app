# Use the official runner image as a base
FROM summerwind/actions-runner:latest

# Switch to root to install packages
USER root

# Install Python and Pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Set python3 as the default 'python' command
RUN ln -s /usr/bin/python3 /usr/bin/python

# Switch back to the runner user
USER runner