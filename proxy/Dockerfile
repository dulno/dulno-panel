ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/panel
RUN ln -s /obfuscation /home/dulno/panel

COPY static /home/dulno/panel/static
COPY obfuscation /home/dulno/panel/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/panel

RUN node /home/dulno/panel/obfuscation/obfuscate.js

FROM nginx

# FIXES CVE-2024-55549  & CVE-2025-24855
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    libxslt1.1=1.1.35-1+deb12u1 \
    && apt-get clean

COPY --from=builder /home/dulno/panel/static /home/dulno/panel/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
COPY proxy/proxy /etc/nginx/sites-enabled/proxy
