from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from io import BytesIO
import controller

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("wietajcie", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(self.path, body)
        res = controller.decode(self.path, body)
        self.send_response(200)
        self.end_headers()
        print(res)
        self.wfile.write(bytes(res, "utf-8"))
        
def run(hostName, serverPort):
    httpd = HTTPServer((hostName, serverPort), Kramakar)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
         httpd.serve_forever()
    except KeyboardInterrupt:
         pass

    httpd.server_close()
    print("Server stopped.")

