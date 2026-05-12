# Istio Gateway Helm Chart

A Helm chart for adeployin and Istion Gateway API resources. Supports both local (KIND) and cloud (GKE) deployments.

## Prerequisites

- Helm 3.x
- Istio installed with Gateway API support
- Gateway API CRDs installed

## Installation 

### Quick Start (KIND)

```bash
# Default configureation uses Nodeport for KIND
helm install gateway ./charts/gateway -n istio-system
```

### Quick Start (GKE)

```bash
helm install gateway /.charts/gateway -n istio-system \
  --set serviceType=LoadBalancer \
  --set nodePort.enabled=false \
  --set hostnamePattern="*.test.com"
```