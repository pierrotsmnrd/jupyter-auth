[![Datalayer](https://raw.githubusercontent.com/datalayer/datalayer/main/res/logo/datalayer-25.svg?sanitize=true)](https://datalayer.io)

# 🛡️ Jupyter Auth

To use this library with GitHub authentication, you need to [create a OAuth app](https://docs.github.com/en/developers/apps/creating-an-oauth-app) and export in your shell environement the client id and the client secret as shell variable:

```bash
export GITHUB_CLIENT_ID=<oauth-app-client-id>
export GITHUB_CLIENT_SECRET=<oauth-app-client-secret>
```

Set the Callback URL to `http://localhost:8888/login` (assuming you are running the Jupyter Server on port 8888).

![](https://raw.githubusercontent.com/datalayer/jupyter-auth/main/docs/source/images/oauth-app-example.png)

## Environment

```bash
conda deactivate && \
  conda remove -y --all -n jupyter-auth
# Create your conda environment.
conda create -y \
  -n jupyter-auth \
  python=3.8 \
  twine \
  nodejs=14.5.0 \
  yarn=1.22.5 \
  cookiecutter
conda activate jupyter-auth
pip install jupyter_packaging
# Install jupyterlab.
pip install jupyterlab==3.0.4
# Install jupyter_auth
pip install -e .
# Build the extension and link for dev in shell 1.
jupyter labextension develop --overwrite
# List extensions.
jupyter labextension list
pip list | grep jupyter-auth
```

```bash
# Run and watch the extension in shell 1.
conda activate jupyter-auth
yarn watch
```

```bash
# Run and watch jupyterlab in shell 2.
# Look at the remote entry javascript, a webpack5 feature.
conda activate jupyter-auth
jupyter lab \
  --watch \
  --ServerApp.jpserver_extensions="{'jupyter_auth': True}" \
  --ServerApp.login_handler_class=jupyter_auth.github.LoginHandler \
  ./examples
```
