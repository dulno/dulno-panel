ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/panel
RUN ln -s /obfuscation /home/dulno/panel

COPY static /home/dulno/panel/static
COPY obfuscation /home/dulno/panel/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/panel

RUN node /home/dulno/panel/obfuscation/obfuscate.js

FROM nginx:latest

# Fix CVE-2024-56406: Update perl-base
RUN apt-get update && \
    apt-get install -y --no-install-recommends perl-base=5.36.0-7+deb12u2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /home/dulno/panel/static /home/dulno/panel/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
COPY proxy/proxy /etc/nginx/sites-enabled/proxy
