echo "Stopping existing containers"
docker-compose down
echo "Building docker images"
docker build -t itm_project .
echo "Running containers"
docker-compose up -d server