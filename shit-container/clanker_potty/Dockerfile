# AlmaLinux 8.10 dev environment for a clanker sandbox.
# It is not a good sanbox, just slightly better than running an agent
# on my host, since the stupid thing does too much.
FROM almalinux:8.10
LABEL description="AlmaLinux 8.10 clanker sandbox"
LABEL version="0.1"
# The most expensive operation at top.
RUN dnf upgrade --assumeyes && \
    dnf group install --assumeyes "Development Tools" && \
    dnf install --assumeyes wget && \
    dnf clean all
ENV UV_COMPILE_BYTECODE=1
RUN useradd --create-home --shell /home/clanker/.local/bin/fish clanker
USER clanker
WORKDIR /home/clanker
CMD ["/home/clanker/.local/bin/fish"]
