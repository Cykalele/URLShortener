import logging
from urllib import request
import azure.functions as func
import requests


from urllib.parse import parse_qs

# This function reacts to POST Requests
def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Python HTTP trigger function processed a request.")
    req_body_bytes = req.get_body()
    logging.info(f"Request Bytes: {req_body_bytes}")
    req_body = req_body_bytes.decode("utf-8")
    logging.info(f"Request: {req_body}")

    long_url = parse_qs(req_body)["long_url"][0]

    #data_to_send = {"long_url": "{long_url}"}
    #request_to_function = requests.post("https://ccurlshortener.azurewebsites.net/api/requestTrigger?code=EnkbZTNMLlnBLurHUj0d8deSqDBs18muyfwAUIJysRvFbjtGtJmqcg==", data={long_url})
    #print(request_to_function.text)

    return func.HttpResponse(
        f"You submitted this information: {long_url}",
        status_code=200,
    )

# This function reacts to GET Requests
"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    long_url = req.params.get('long_url')
    if not long_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            long_url = req_body.get('long_url')

    if long_url:
        return func.HttpResponse(f"Hello {long_url}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )
"""