from flask import Flask, render_template, request
import ibm_boto3
from ibm_botocore.client import Config, ClientError
import os

app = Flask(__name__)

# IBM Cloud Object Storage Configuration
COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"  # Replace with your endpoint
COS_API_KEY_ID = "2-sQqkMwrn7GtCGDlm5XsFgkh3YzDlZ6MMdyrA_8Bey9"  # Replace with your API key
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/0bb4d59c58f057ca240dd82f9bf0ca02:2ae624a1-15a0-4a2b-a8dd-c91dfe4e681c::"  # Replace with your service instance CRN
COS_BUCKET_NAME = "nov4-upload-app-bucket-1"  # Replace with your bucket name

# Initialize the IBM Cloud Object Storage client
cos = ibm_boto3.client("s3",
                       ibm_api_key_id=COS_API_KEY_ID,
                       ibm_service_instance_id=COS_INSTANCE_CRN,
                       config=Config(signature_version="oauth"),
                       endpoint_url=COS_ENDPOINT)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        try:
            # Use put_object to upload the file to Cloud Object Storage
            cos.put_object(
                Bucket=COS_BUCKET_NAME,
                Key=file.filename,
                Body=file
            )
            return f"File {file.filename} uploaded to Cloud Object Storage successfully!"
        except ClientError as e:
            return f"Client error: {e}"
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
