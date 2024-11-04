# Steps to run locally

source venv/bin/activate
python app.py
Navigate to http://127.0.0.1:5000

# Build the image

podman build -t upload-app:try-22 .

# Run the image locally (optional)

podman run --platform linux/arm64 -d -p 5022:5000 upload-app:try-22

# Push image to Docker Hub


podman push upload-app:try-22 docker.io/mwlinnem/upload-app:try-22

# Deploy image from DockerHub to Code Engine

ibmcloud code-engine application create --name foo --port 5000 --image docker.io/mwlinnem/upload-app:oct-10-v2-9