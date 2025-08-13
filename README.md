# MCP Policy Webform (Flask)

A minimal Flask web application that collects:

- Operating system (Windows, Linux, Mac)
- IDE (windsurf, cursor)
- Freeform policy requirements

It validates inputs and shows a styled summary page. The UI is inspired by Snyk’s design language.

## Requirements

- Python 3.10+
- pip

## Quick start

### 1) Run the start script
```bash
chmod +x start_app.sh
./start_app.sh
```

## Detailed Setup

### 1) Clone the repo and cd into it
```bash
git clone git@github.com:brookecastleberry/MCP_Policy_DB.git
```
```
cd MCP_Policy_DB
```
### 2) Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
###3) Install dependencies
```bash
pip install -r requirements.txt
```
### 4a) Run directly (defaults to port 
5000)
```bash
python app.py
# Open http://127.0.0.1:5000
```

### 4b) If port 5000 is in use, run via Flask CLI on an alternate port
```bash
FLASK_APP=app:app FLASK_RUN_HOST=127.0.0.1 FLASK_RUN_PORT=5050 flask run
# Open http://127.0.0.1:5050
```

## Using the app

1) Open the app in your browser
2) Select your operating system and IDE
3) Describe the policy types you need (e.g., access control, data retention)
4) Submit to view a formatted summary

## Killing the app

Press CTRL+C in the running terminal

## Security notes

- Debug mode is disabled by default (`debug=False`).
- Dependencies are pinned in `requirements.txt`.
- Recommended: run security scans locally (requires Snyk CLI and authentication):

```bash
# Static code analysis
snyk code test

# Open source dependencies (SCA)
snyk test --file=requirements.txt
```

Learn more about Snyk’s platform at https://snyk.io/.

## Production

Use a production WSGI server instead of the development server, e.g.:

```bash
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

Behind a reverse proxy (e.g., Nginx) add TLS, logging, and rate limiting as needed.

## Project structure

```
.
├── app.py
├── requirements.txt
├── static/
│   └── snyk.css
└── templates/
    ├── index.html
    └── result.html
```