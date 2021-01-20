import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './handler'

import { AuthWidget } from './widget';

import { reactIcon } from '@jupyterlab/ui-components';

function request(path: string, widget: AuthWidget) {
  return requestAPI<any>(path)
    .then(data => {
      console.log('Got a response from the jupyter_auth server API', data);
      widget.setUsers(data)
    })
    .catch(reason => {
      console.error(
        `The jupyter_auth server API appears to be missing.\n${reason}`
      );
    });
}

const auth: JupyterFrontEndPlugin<void> = {
  id: 'jupyter-auth',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    const widget = new AuthWidget();
    widget.id = 'jupyter-auth'
    widget.title.icon = reactIcon;
    app.shell.add(widget, 'left', { rank: 300 })
    request('users', widget)
  }

};

export default auth;
