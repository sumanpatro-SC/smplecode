from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

class StudentRouter(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path

        # if path in ("/", "index.html"):
        #     return serve_html(self)

        # if path.startswith("/static/"):
        #     return serve_static(self)

        if path == "/api/students":
            return get_all_students(self)

        # API: Get student by ID
        if path.startswith("/api/students/"):
            student_id = int(path.split("/")[-1])
            return get_student(self, student_id)

        return send_404(self)

    def do_POST(self):
        if self.path == "/api/students":
            return create_student(self)
        return send_404(self)
