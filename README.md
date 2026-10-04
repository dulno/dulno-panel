<div align="center">
  <img src="https://dulno.com/static/img/logo-light.webp" alt="logo" width="128"  height="auto" />

  <h1><b>Dulno - Panel</b><br><br></h1>

</div>

This is the repository that manages all functionalities of the web panel in the frontend and the middleware. It provides the central interface for employees to answer tickets and emails. It also performs other administrative tasks.

## Status

|      | Pipeline status                                                       |
|------|-----------------------------------------------------------------------|
| main | ![](https://github.com/dulno/dulno-panel/actions/workflows/ci.yml/badge.svg?branch=main) |
| dev  | ![](https://github.com/dulno/dulno-panel/actions/workflows/ci.yml/badge.svg?branch=dev)  |

## Installation

```bash
python -m venv env

source env/bin/activate

pip install gunicorn -r requirements.txt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```


## License

© Dulno. Licensed under [CC BY-NC-SA 4.0](LICENSE): free for non-commercial use with attribution to Dulno, modifications must be shared under the same license. Third-party code (e.g. under `static/dependency/`) keeps its own license.
