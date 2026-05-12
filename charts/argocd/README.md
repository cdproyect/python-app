# Installing ArgoCD chart

Follow instructions [here](https://github.com/argoproj/argo-helm/tree/main/charts/argo-cd#installing-the-chart)

```sh
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm upgrade --install argo-cd argo/argo-cd -n argocd --create-namespace -f ./charts/argocd/values.yaml