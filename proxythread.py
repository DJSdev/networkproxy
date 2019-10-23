import threading
import app2server
import server2app
import sys


class ProxyThread(threading.Thread):

    def __init__(self, host, server, port):
        super(ProxyThread, self).__init__()
        self.from_host = host
        self.to_server = server
        self.port = port
        print(f'Starting proxy on {self.port}')

    def run(self):
        while True:
            self.a2s = app2server.App2Server(self.from_host, self.port)
            self.s2a = server2app.Server2App(self.to_server, self.port)
            self.a2s.server = self.s2a.serv_ssock
            self.s2a.app = self.a2s.app
            self.a2s.start()
            self.s2a.start()


hosting = "127.0.0.1"
cnn = "151.101.65.67"
port = 443

proxy_server = ProxyThread(hosting, cnn, port)
proxy_server.start()

while True:
    try:
        cmd = input('$ ')
        if cmd[:4] == 'quit':
            sys.exit(0)
    except Exception as e:
        break

