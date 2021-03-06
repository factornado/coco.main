import yaml
import os
import time
from tornado import ioloop, web, httpserver, httpclient
import logging

from utils import Config

config = Config('config.yml')

logging.basicConfig(
    level=10,
    filename=config.conf['log']['file'],
    format='%(asctime)s (%(filename)s:%(lineno)s)- %(levelname)s - %(message)s',
    )
logging.Formatter.converter = time.gmtime
logging.getLogger('tornado').setLevel(logging.WARNING)
logging.info('='*80)


class Info(web.RequestHandler):
    def get(self):
        self.write(config.conf)


class SomeHandler(web.RequestHandler):
    def get(self, param=''):
        self.write(
            "Hello from service {}. "
            "You've asked for uri {}\n".format(
                config.conf['name'], param))

app = web.Application([
    ("/(swagger.json)", web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
    ("/swagger", web.RedirectHandler, {'url': '/swagger.json'}),
    ("/info", Info),
    ("/(.*)", SomeHandler),
    ])

if __name__ == '__main__':
    port = config.get_port()  # We need to have a fixed port in both forks.
    logging.info('Listening on port {}'.format(port))
    server = httpserver.HTTPServer(app)
    server.bind(config.get_port(), address='0.0.0.0')
    server.start(config.conf['threads_nb'])
    ioloop.IOLoop.current().start()
