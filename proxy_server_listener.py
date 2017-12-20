import socket
import server_parser
import http_forwarder
import requests
import os


def server_listener(server_IP,port):
    os.system("lsof -i :80 >\\dev\\null")
    serversocket = set_up_server(server_IP,port)
    while 1:
        #accept connections from outside
        try:
            (clientsocket, address) = serversocket.accept()
        except:
            os.system("lsof -i :80 >\\dev\\null")
            print("Server exited, server not listeing, connection refused!")
            break
        #now do something with the clientsocket
        #in this case, we'll pretend this is a threaded server
        text_request = clientsocket.recv(10000)
        print(text_request)
        data = http_forwarder.forwarder(text_request)
        clientsocket.send(data)
        ##serversocket.close()

def set_up_server(server_IP,port):
    #create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to a public host,
    # and a well-known port
    serversocket.bind((server_IP, port))
    #become a server socket
    serversocket.listen(5)
    return serversocket

def main():
    server_listener("localhost",80)

main()
