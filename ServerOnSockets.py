from socketserver import TCPServer, StreamRequestHandler
from time import ctime

# Globals
HOST = ''
PORT = 23456
ADDR = (HOST, PORT)


class MyRequestHundler(StreamRequestHandler):
    def handle(self):
        print("...connect", self.client_address) #Connecting to the client
        self.wfile.write(' [%s] %s' % (ctime(),
        self. rfile. readline ()))

#Waiting for client connection
tcp_server = TCPServer(ADDR, MyRequestHundler,)
print("Waiting for connection...")
tcp_server. serve_forever()
