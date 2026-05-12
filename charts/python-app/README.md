# Python App Helm Chart

A helm chart for deployeing a simple API using python falsk applicatoin on Kubernetes with Istio Gateway API support.

## Prerequesites 

- Helm 3.x
- Istio with Gateway API support installed
- Gateway API CRDs installed

## Installation 

### Quick Start (KIND)

1. Generate self-signed certificate
    ```sh
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
      -keyout tls.key -out tls.crt \
      -subj "/CN=*.test.com"
    ```
1. Create the secret in istio-system
    ```sh
    kubectl create secret tls gateway-tls \
      --cert=tls.crt \
      --key=tls.key \
      -n istio-system
    ```
1. Install the chart
    ```sh
    helm install python-app ./chats/python-app

