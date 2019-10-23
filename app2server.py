import threading
from ssl import *
import socket


class App2Server(threading.Thread):

    def __init__(self, host, port):
        super(App2Server, self).__init__()
        self.server = None
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)
        self.cli_ssock = wrap_socket(self.sock,
                         certfile="../TestCertKey/cacert.pem",
                         keyfile="../TestCertKey/privkey.key",
                         server_side=True)
        self.app, self.addr = self.cli_ssock.accept()

    def run(self):
        while True:
            try:
                data = self.app.recv(20971520)
                if data:
                    print(f"App -> Server: {data}")
                    self.server.sendall(data)
            except Exception as e:
                print(e)
                break
