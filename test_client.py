import requests

try:
    r = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList")
    headers = r.headers
    body = r.text
    text_request = ""
    for i in headers:
        text_request+=i + ": " + headers[i]+"\r\n"
    total_text_request = text_request + "\r\n" + body

    print(total_text_request)
except:
    print("Error request.")
