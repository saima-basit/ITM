echo "Stopping existing containers"
docker-compose down
echo "Building docker images"
docker build -t itm_project .
echo "Running containers"
docker-compose up -d server

docker run -itd -p 8888:1111 itm_project