# How to deploy ARC (actions-runner-controller)

1️⃣ Install cert-manager in your cluster
  ```sh
  kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml
  ```
2️⃣ Deploy and Configure ARC
  1. Add helm repository
    ```sh
    helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
    ```
  1. Install Helm chart
    ```sh
    export GITHUB_PAT="REPLACE_YOUR_TOKEN_HERE"
    helm upgrade --install --namespace actions-runner-system --create-namespace\
      --set=authSecret.create=true\
      --set=authSecret.github_token="${GITHUB_PAT}"\
      --wait actions-runner-controller actions-runner-controller/actions-runner-controller
    ```
3️⃣ Create the GitHub self hosted runners and configure to run against your repository.

```yaml
cat << EOF | kubectl apply -n actions-runner-system -f -
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: self-hosted-runners
spec:
  replicas: 1
  template:
    spec:
      repository: cdproyect/python-app
EOF
````
<sub> *note:- Replace "cdproyect/python-app" with the name of the GitHub repository the runner will be associated with. </sub>

## How can we reach to argocd server from the runners

```sh
k exec -it self-hosted-runners-zqrn9-jzt7j -- sh
```
From the pod try to reach your svc
```sh
$curl argo-cd-argocd-server.argocd
```
# references
https://github.com/actions/actions-runner-controller/blob/master/docs/quickstart.md