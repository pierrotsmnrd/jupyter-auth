import os
import jinja2

from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin
from jupyter_server.utils import url_path_join

from .handlers import DefaultHandler, ExampleHandler


class JlabExtensions(ExtensionApp):

    # The name of the extension.
    name = "jupyter_auth"

    # The url that your extension will serve its homepage.
    extension_url = '/jupyter_auth/default'

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    def initialize_settings(self):
        self.log.info(f'{self.name} is enabled.')

    def initialize_handlers(self):
#        host_pattern = ".*$"
#        base_url = self.settings["base_url"]
#        route_pattern = url_path_join(base_url, "jupyter_auth", "get_example")
#        self.handlers.extend([
#            (r'/{}/default'.format(self.name), DefaultHandler),
#            (route_pattern, RouteHandler),
#        ])
        self.handlers.extend([
            (r'/jupyter_auth/default', DefaultHandler),
            (r'/jupyter_auth/get_example', ExampleHandler),
        ])

# Entry Point Definition

main = launch_new_instance = JlabExtensions.launch_instance
