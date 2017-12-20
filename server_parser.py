import mimetools
from StringIO import StringIO

##text_request = 'GET /search?sourceid=chrome&ie=UTF-8&q=ergterst HTTP/1.1\r\nHost: www.google.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: python-requests/2.13.0\r\n'


'''

GET / HTTP/1.1
Host: localhost
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.13.0'''

def parser(text_request):
# Pop the first line for further processing
    request, text_request = text_request.split('\r\n', 1)
# Get the headers
    m = mimetools.Message(StringIO(text_request))
# Add request information
    m.dict['method'], m.dict['path'], m.dict['http-version'] = request.split()
    if(m['method']=="GET"):
        return(m['path'])

#parser(text_request)
