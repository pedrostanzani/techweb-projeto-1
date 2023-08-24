from pathlib import Path
import json

def extract_route(raw_request):
    lines = raw_request.splitlines()
    if len(lines) == 0:
        return None
    first_line = lines[0]

    path = first_line.split()[1]
    if path[0] == '/':
        path = path[1:]

    return path

def read_file(path: Path):
    with open(str(path), 'rb') as file:
        content = file.read()
    return content

def load_template(template_filename):
    path = f'templates/{template_filename}'
    with open(path, 'r') as file:
        content = file.read()
    return content

def build_response(body='', code=200, reason='OK', headers=''):
    headers = f"\n{headers}" if headers else ""
    return f'HTTP/1.1 {code} {reason}{headers}\n\n{body}'.encode()
