#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests, os, subprocess

hostName = subprocess.getoutput('hostname --ip-address')
serverPort = int(os.getenv('PORT', ''))

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        response = requests.get("https://appsupport.abc-prod.net.au/Prod/listen/newsbulletin")
        bulletin = response.json()['bulletins'][0]['url']

        self.send_response(302)
        self.send_header('Location', bulletin)
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")