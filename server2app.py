import threading
from ssl import *
import socket
import gzip


class Server2App(threading.Thread):

    def __init__(self, host, port):
        super(Server2App, self).__init__()
        self.app = None
        self.port = port
        self.host = host

        self.ctx = create_default_context()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_ssock = wrap_socket(self.server, server_side=False)
        self.serv_ssock.connect((self.host, self.port))

    def run(self):
        while True:
            try:
                data = self.serv_ssock.recv(20971520)
                print(f"Server -> App: {data}")

                self.app.sendall(data)
            except Exception as e:
                print(e)
                break
