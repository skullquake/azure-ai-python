import json
import azure.functions as func
def main(req: func.HttpRequest) -> func.HttpResponse:
    resp = {
        "status": "success",
        "message": "testWarren"
    }
    return func.HttpResponse(
        json.dumps(resp),
        status_code=200,
        mimetype="application/json"
    )
