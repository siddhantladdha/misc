# AlmaLinux 8.10 dev environment with uv and build tools
# primarily for building python appimages and dotfile
# bundles.
FROM almalinux:8.10
LABEL description="AlmaLinux 8.10 build environment"
LABEL version="0.4"
# The most expensive operation at top.
RUN dnf upgrade --assumeyes && \
    dnf group install --assumeyes "Development Tools" && \
    dnf install --assumeyes wget && \
    dnf clean all
ENV UV_COMPILE_BYTECODE=1
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ARG FISH_VERSION=4.6.0
ADD https://github.com/fish-shell/fish-shell/releases/download/$FISH_VERSION/fish-$FISH_VERSION-linux-x86_64.tar.xz /usr/local/bin/fish.tar.xz
RUN cd /usr/local/bin && \
    tar --extract --xz --verbose --file=fish.tar.xz && \
    rm -r fish.tar.xz
# checksum not working. TODO: Debug
# ADD --checksum=sha256:497c9c4e3fb3c006fe9d2c9a5a5447c1c90490b6b4ce6bfaf75e53b495c82f37
RUN useradd --create-home neo
USER neo
WORKDIR /home/neo
CMD ["/bin/bash"]
