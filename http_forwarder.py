import requests
import server_parser

##MESSAGE="GET /service/publicXMLFeed?command=agencyList HTTP/1.1\r\nHost: localhost\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n"


def forwarder(text_request):
    path = server_parser.parser(text_request)
    try:
        r = requests.get("http://webservices.nextbus.com" + path)
        headers = r.headers
        body = r.text
        text_request = ""
        for i in headers:
            text_request+=i + ": " + headers[i]+"\r\n"
        total_text_request = text_request + "\r\n" + body

        return total_text_request
    except:
        print("Error request.")
