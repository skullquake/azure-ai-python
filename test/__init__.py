import json
import azure.functions as func
#import os
def main(req: func.HttpRequest) -> func.HttpResponse:
    #AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    #AZURE_CONTAINER_NAME = os.environ.get('AZURE_CONTAINER_NAME')
    #AZURE_SAS_TOKEN = os.environ.get('AZURE_SAS_TOKEN')
    #AZURE_ENDPOINT = os.environ.get('AZURE_ENDPOINT')
    #AZURE_SUBSCRIPTION_KEY = os.environ.get('AZURE_SUBSCRIPTION_KEY')
    #AZURE_MODEL_ID = os.environ.get('AZURE_MODEL_ID', 'prebuilt-invoice')
    #AZURE_API_VERSION = os.environ.get('AZURE_API_VERSION', '2024-11-30')
    resp = {
        "status": "success",
        "message": "test9"#,
        #"AZURE_ACCOUNT_NAME":AZURE_ACCOUNT_NAME,
        #"AZURE_CONTAINER_NAME":AZURE_CONTAINER_NAME,
        #"AZURE_SAS_TOKEN":AZURE_SAS_TOKEN,
        #"AZURE_ENDPOINT":AZURE_ENDPOINT,
        #"AZURE_SUBSCRIPTION_KEY":AZURE_SUBSCRIPTION_KEY,
        #"AZURE_MODEL_ID":AZURE_MODEL_ID,
        #"AZURE_API_VERSION":AZURE_API_VERSION
    }
    return func.HttpResponse(
        json.dumps(resp),
        status_code=200,
        mimetype="application/json"
    )
