class MyHnadler(SimpleHTTPRequestHandler)

def do_GET(self):
    it self.path =='/':
      self.path = 'index.html'
    return supur().do_GET()

if __name__ == "__main__":
    erver = HTTPServer(('localhoust',8000)MyHhandler):
    print("serving on https://localhoust:8000")
    server.server_forever()
    