import logging

import azure.functions as func
from urllib.parse import parse_qs


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body_bytes = req.get_body()
    logging.info('Request Bytes: {req_body_bytes}')
    req_body = req_body_bytes.decode('utf-8')
    logging.info('Request Bytes: {req_body}')

    long_url = parse_qs(req_body)['long_url'][0]

    return func.HttpResponse(
        'You submitted this information: {long_url}', status_code=200
    )
    """url = req.params.get('long_url')
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
        )"""
