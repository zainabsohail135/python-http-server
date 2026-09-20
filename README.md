# Simple HTTP Server in Python

A basic web server built from scratch using Python's `socket` module, based on [this tutorial](https://joaoventura.net/blog/2017/python-webserver/).

## Features
- Serves static files from the `htdocs/` folder
- Returns `404` for missing files
- Blocks path traversal (`../`) with a `403`

## Run it
```
python httpserver.py
```
Then open http://localhost:8000