FROM mysql:8.0.43-debian

RUN apt-get update && \
    apt-get install -y percona-toolkit
