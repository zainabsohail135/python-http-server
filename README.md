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


Code/Process explanation:

1. Opens the counter. It creates a socket, claims port 8000, and starts listening.
2. Waits for a customer. accept() pauses until a browser connects.
3. Reads the order. The browser sends text like GET /ipsum.html HTTP/1.1. Your code pulls out /ipsum.html, the file being asked for.
4. Handles the bare address. If the order is just /, it means the homepage, so it uses /index.html.
5. Checks the order is safe. It determines the file's real location and ensures it's within htdocs. If someone tries ../httpserver.py to reach secret files, they get 403 Forbidden.
6. Fetches the food. It tries to read the file. If it exists, the reply is 200 OK plus the file's contents. If it doesn't, the reply is 404 NOT FOUND.
7. Serves and closes. It sends the reply, ends the connection, and goes back to waiting for the next customer.
