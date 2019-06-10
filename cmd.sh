# DOCKER
docker build -t demo-docker .
docker run -p 5000:5000 demo-docker
docker login
docker tag demo-docker:latest pminder/demo-docker:v1
docker push pminder/demo-docker:v1
docker run pminder/demo-docker:v1

# KUBERNETES
kubectl run demo-kubernet --image=demo-docker:v1 --port=8181
kubectl expose deployment/demo-kubernet --type="NodePort" --port=5000
kubectl scale deployment/demo-kubernet --replicas=4
kubectl set image deployment/demo-kubernet demo-kubernet=demo-docker:v2
