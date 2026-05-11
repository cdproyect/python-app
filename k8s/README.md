# Deploy application in Local Kubernetes Cluster (KIND)

## Push Image to Docker Hub

1. Tag your image to match your docker registry
    ```sh
    docker tag python-app:v1 cdproyect/python-app:v1
    ```

1. Push your image
    ```sh
    docker push cdproyect/python-app:v1
    ```

## Create KIND Cluster

```sh
kind create cluster --config ./kind_cfg/kind.yaml
```

## Deploy your application

```sh
kubectl apply -f k8s/deploy.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
## If you want to set up HTTPS follow GATEWAY.md instructions

### This is required for KIND to map the ports for the Gateway to the ports used in the kind.yaml configuration
kubectl apply -f k8s/svc-gateway.yaml
```


## Clean

```sh
kubectl delete -f k8s/deploy.yaml
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/gateway.yaml
kind delete cluster
```