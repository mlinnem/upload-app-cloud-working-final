# Steps to run locally

source venv/bin/activate
python app.py
Navigate to http://127.0.0.1:5000

# Build the image

## (Secret flaw)
podman build  -t [UNIQUE_IMAGE_NAME] .

## (Correct)
podman build --platform linux/amd64 -t [UNIQUE_IMAGE_NAME] .

# Push image to Docker Hub

podman push [UNIQUE_IMAGE_NAME] docker.io/mwlinnem/[UNIQUE_IMAGE_NAME]

# Deploy image from DockerHub to Code Engine

ibmcloud code-engine application create --name [UNIQUE_APP_NAME] --port 5000 --image docker.io/mwlinnem/[UNIQUE_IMAGE_NAME] --wait-timeout 180