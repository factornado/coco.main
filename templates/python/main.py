import yaml
from tornado import ioloop, web, httpserver

conf = yaml.load(open('config.yml'))

service_name = 'main'


def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class SomeHandler(web.RequestHandler):
    def get(self, param=''):
        self.write(
            "Hello from service {}. "
            "You've asked for uri {}\n".format(
                conf['name'], param))

app = web.Application([
    ("/(.*)", SomeHandler),
    ])

# port = get_open_port()  # Use this to get a random port.
port = 8001
print('Listening on port', port)

server = httpserver.HTTPServer(app)
server.bind(port, address='0.0.0.0')
server.start(conf['threads_nb'])
ioloop.IOLoop.current().start()
