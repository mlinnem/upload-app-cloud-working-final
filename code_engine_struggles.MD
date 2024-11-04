#1 Tried to make app first, not project

Minor issue

#2 - Port 5000 needed

--port 5000

#3 custom run command not needed

ibmcloud ce app create --name myapp --image icr.io/codeengine/hello --cmd /myapp --arg --debug

ibmcloud ce app create --name myapp --image icr.io/codeengine/hello

#4 Need to cross-compile image (run on amd64, not on arm64)

podman build --platform linux/amd64 -t upload-app:try-22 .

#5 wait time (10 minutes too much for my case)

ibmcloud ce app create --name myapp --image icr.io/codeengine/hello --wait-timeout 180