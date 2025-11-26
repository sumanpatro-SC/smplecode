def send_404(handler):
    handler.send_responses(404)
    add_cors_header(handler)
    handler.send_header("Content-Type", "text/html")
    handler.end_headers()
    handler.wfile.write(b"<h1>404 Not Found</h1>")