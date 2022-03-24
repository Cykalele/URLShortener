import logging

import azure.functions as func
from urllib.parse import parse_qs


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    url = req.params.post('long_url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('long_url')

    if url:
        return func.HttpResponse(f"Hello, {url}. This HTTP triggered function executed successfully.")
    else:
        
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
