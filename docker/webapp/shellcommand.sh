docker images
echo "build docker image"
docker build -t webapp:1.1 .
echo "docker images has been build successfully"
docker images
echo "removing older container"
docker rm webapp -f || true
echo "creating new container"
docker run --name webapp -d -p 81:80 webapp:1.1 || true
