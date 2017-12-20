

Reverse Proxy Server


This is a a python based server and consists of different scripts. It has a dependency on following modules :
1. requests
2. socket
3. mimetools
4. StringIO

So, kindly make sure you have those dependencies install. Here is a quick command.

"pip install socket requests mimetools StringIO"

The application is in 3 scripts :
1. proxy_server_listener.py - The code which keeps listening on localhost, port 80. This runs on continuos loop and forwards the request to the backend NEXTBus API.

2. http_forwarder - This script send get request to NEXTBus API.

3. server_parser - parses the body of incoming client request, pulls out the "path" from HTTP request. This is later used to query the backend.

Issues :

Port 80 is already running : Facing issues with this, so please use
"lsof -i :80 >\\dev\\null"
to kill the process on the port.

Not able to render the HTTP request completely, so the output you see in the browser is a pure HTTP response.

How to run and test :
1. Run the server using "python proxy_server_listener.py"
2. Browse a NEXTBus link from localhost. (replace webservices.nextbus.com with localhost)

Expected output :
You should see the response from the nextbus server.
