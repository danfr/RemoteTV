import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn


class Server:
    httpd = None

    def start(self, port):
        print('starting server...')

        # Server settings
        server_address = ('127.0.0.1', port)
        self.httpd = ThreadedHTTPServer(server_address, RequestHandler)
        print('running server...')
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        code = Worker.manage_command(form)

        # Begin the response
        self.send_response(code)
        return
