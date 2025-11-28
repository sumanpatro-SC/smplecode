from http.server import HTTPServer
from router import StudentRouter
from database.connection import init_database 


# Changed default port from 8000 to 8001
def run_server(port=8001): 
    # Initialize the database before starting the server
    init_database() 
    
    server = HTTPServer(("",port),StudentRouter)
    print(f"Server running at http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()