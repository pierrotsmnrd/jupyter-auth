import json

from jupyter_server.base.handlers import JupyterHandler, APIHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin, ExtensionHandlerJinjaMixin
from jupyter_server.base.zmqhandlers import WebSocketMixin

import tornado
from tornado.websocket import WebSocketHandler, websocket_connect
from tornado.ioloop import IOLoop

class DefaultHandler(ExtensionHandlerMixin, JupyterHandler):

    def get(self):
        # The name of the extension to which this handler is linked.
        self.log.info("Extension Name in {} Default Handler: {}".format(
            self.name, self.name))
        self.write('<h1>Jupyter Auth Extension</h1>')
        self.write('Config in {} Default Handler: {}'.format(
            self.name, self.config))


class ExampleHandler(APIHandler):

    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
#        print(self.get_sessions()[self.get_session_id()]['user'])
        for s in self.get_sessions().values():
            print(f"--- {s['user']}")
        self.finish(json.dumps({
            "data": "This is /jupyter_auth/get_example endpoint!",
            "session_id": self.get_session_id(),
            "session_counts": self.get_sessions_count(),
            "user": self.get_current_user()
        }))
