FROM quay.io/astronomer/astro-runtime:11.0.0
# ENV PIP_NO_VERIFY 1
# USER root
# COPY ./ca-bundle.trust.crt /usr/local/share/ca-certificates/dxc/
# COPY ./ca-bundle.crt /usr/local/share/ca-certificates/dxc/
# COPY ./ca-certificates.crt /usr/local/share/ca-certificates/dxc/
# RUN update-ca-certificates
# USER astro
