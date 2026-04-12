# AlmaLinux 8.10 dev environment with uv and build tools
# primarily for building python appimages and dotfile
# bundles.
FROM almalinux:8.10
LABEL description="AlmaLinux 8.10 build environment"
LABEL version="0.1"
ENV UV_COMPILE_BYTECODE=1
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN dnf upgrade --assumeyes && \
    dnf group install --assumeyes "Development Tools" && \
    dnf clean all
    # dnf install --assumeyes wget # Evaluate if needed.
RUN useradd --create-home neo
USER neo
WORKDIR /home/neo
CMD ["/bin/bash"]
