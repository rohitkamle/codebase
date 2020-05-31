# Download Helm using below command
wget https://get.helm.sh/helm-v3.1.2-linux-amd64.tar.gz

# untar file
tar -zxvf  helm-v3.1.2-linux-amd64.tar.gz

# move file to local bin
mv linux-amd64/helm /usr/local/bin/helm

# check helm 
Helm help

# add ingress controller repo
helm repo add stable https://kubernetes-charts.storage.googleapis.com/

# install restapi ingress controller
helm install demo-ingress stable/nginx-ingress \
    --set controller.replicaCount=1 \
    --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux \
    --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux || true