#!/usr/bin/env python

import sys
if sys.version_info[0] < 3:
    import SocketServer as socketserver
else:
    import socketserver

class MeshHandler(socketserver.BaseRequestHandler):

    def handle(self):
        req = self.request.recv(1024).strip()
        if not req:
            return
        resp = req[0:4] + req[10:16] + req[4:10] + req[16:]
        self.request.sendall(resp)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 7000
    server = socketserver.TCPServer((HOST, PORT), MeshHandler)
    server.allow_reuse_address = True
    server.serve_forever()

