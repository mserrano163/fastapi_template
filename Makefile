# Docker image name
IMAGE_NAME = your_image_name

# Docker container name
CONTAINER_NAME = your_container_name

# Build the docker image
build:
	sudo docker build -t $(IMAGE_NAME):prod .

# Run the Docker container
run:
	sudo docker run -p 8080:8000 -v $(PWD):/app --name $(CONTAINER_NAME)_$(shell date +%Y%m%d%H%M%S) $(IMAGE_NAME):prod \
	uvicorn app:your_app_name --host 0.0.0.0 --port 8000