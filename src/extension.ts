import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './handler'

const server: JupyterFrontEndPlugin<void> = {
  id: 'jupyter-auth',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    requestAPI<any>('get_example')
      .then(data => {
        console.log('Got a response from the server API', data);
      })
      .catch(reason => {
        console.error(
          `The @datalayer/server-extension server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default server;
