[![Datalayer](https://raw.githubusercontent.com/datalayer/datalayer/main/res/logo/datalayer-25.svg?sanitize=true)](https://datalayer.io)

# 🛡️ Jupyter Auth

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
```

```bash
# Install jupyterlab.
pip install jupyterlab==3.0.4
# ...or alternatively, clone and build jupyterlab from source.
git clone https://github.com/jupyterlab/jupyterlab --depth 1 -b master && \
  cd jupyterlab && \
  pip install -e . && \
  jupyter lab build && \
  cd ..
```

```bash
pip install ipywidgets==7.6.0
```

## Develop

```bash
# Build the extension and link for dev in shell 1.
jupyter labextension develop --overwrite
```

```bash
# List extensions.
jupyter labextension list
pip list | grep jupyter-auth
```

```bash
# Run and watch the extension in shell 1.
yarn watch
```

```bash
# Run and watch jupyterlab in shell 2.
# Look at the remote entry javascript, a webpack5 feature.
conda activate jupyter-auth && \
  jupyter lab \
    --watch \
    --ServerApp.token= \
    --ServerApp.jpserver_extensions="{'jupyter_auth': True}" \
    ./examples
```

```bash
# Only if you have build jupyterlab from source.
# Run and watch jupyterlab in shell 2.
# Look at the remote entry javascript, a webpack5 feature.
conda activate jupyter-auth && \
  jupyter lab \
    --watch \
    --dev-mode \
    --ServerApp.token= \
    --ServerApp.jpserver_extensions="{'jupyter_auth': True}" \
    --extensions-in-dev-mode \
    ./examples
```

## Build

```bash
# Generate sourcemaps.
jupyter labextension build --development=True .
jupyter lab build --minimize=False
```

```bash
# Do not generate sourcemaps.
jupyter labextension build .
jupyter lab build
```

## Publish

```bash
cd jupyter_auth && \
  yarn build:lib && \
  npm publish --access public
```

```bash
cd jupyter_auth && \
  pip install -e . && \
  python setup.py sdist bdist_wheel && \
  twine upload dist/*
```

## Use

```bash
conda deactivate && \
  conda remove -y --all -n jupyter-auth-user
# Create your conda environment.
conda create -y \
  -n jupyter-auth-user \
  python=3.8 \
  nodejs=14.5.0
conda activate jupyter-auth-user
pip install --pre jupyterlab==3.0.3
```

```bash
pip install jupyterlab_widgets==1.0.0a6
jupyter labextension list
# Check the Extension Manager.
jupyter lab --notebook-dir=~/notebooks
```

```bash
# https://pypi.org/project/jupyterlab-geojs/#history
pip search "jupyterlab extension"
pip search "JupyterLab3"
```

```bash
pip install @datalayer/jupyter-auth
jupyter labextension list
jupyter lab --notebook-dir=~/notebooks
```

## Credits

This folder contains code taken from following sources:

- https://github.com/deshaw/jupyterlab-execute-time
- https://github.com/ibqn/jupyterlab-codecellbtn
- https://github.com/jtpio/jupyterlab-cell-flash
- https://github.com/jtpio/jupyterlab-python-file
- https://github.com/jtpio/jupyterlab-theme-toggle
- https://github.com/jtpio/jupyterlab-topbar
- https://github.com/jupyterlab/extension-examples
- https://github.com/nersc/jupyterlab-recents
- https://github.com/voila-dashboards/voila
- https://github.com/yuvipanda/jupyterlab-nbmetadata
