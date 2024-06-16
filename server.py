from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import json
import client

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3000

class NeuralHTTP(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
    
    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message":"Hello, world!"}')
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        # Read the post data
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            response_message = f"Received JSON Data: {data}"
        except json.JSONDecodeError:
            response_message = f"Received raw data: {post_data.decode("utf-8")}"
        print(response_message)
        
        self.send_response(200, "Success")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        # Fetching data from flipkart site
        info = client.fetchingInfo(data['key'])
        
        # json.dumps() converts Python objects into a JSON string And encode('utf-8) is like bytes() function both do the same thing.
        self.wfile.write(json.dumps(info).encode("utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print(f"[Listening] Server Is Running On {HOST}:{PORT}")
server.serve_forever()
server.server_close()
print("[Stopped] Server Stopped")
