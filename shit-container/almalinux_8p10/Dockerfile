FROM almalinux:8.10
RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y wget
RUN useradd -m neo
USER neo
WORKDIR /home/neo
CMD ["/bin/bash"]
