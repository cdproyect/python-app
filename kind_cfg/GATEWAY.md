# Set up Kubernetes Gateway API

Follow [Setup instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/#setup)

1. Install the Gateay API CRDs
    ```sh
      kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
      { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.4.0" | kubectl apply -f -; }
    ```
1. Install Istio using the minimal profile
Install
    ```sh
    istioctl install --set profile=minimal -y
    ```
1. Deploy gateway.yaml
    ```sh
    kubectl apply -f gateway.yaml
    ```
1. Deploy svc-gateway.yaml (I use [this reference](https://ryandeangraham.medium.com/istio-gateway-api-nodeport-c598a21c4c95))
    ```sh
    kubectl apply -f svc-gateway.yaml
    ```

## Set up HTTPS

This is just for a lab environment

### 1. Generate self-signed certificate

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=*.test.com"
```
### 2. Create the secret in istio-system

```sh
kubectl create secret tls gateway-tls \
  --cert=tls.crt \
  --key=tls.key \
  -n istio-system
```

# References

https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/
