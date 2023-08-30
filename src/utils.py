from pathlib import Path
import json

class_names = {
    'brown':  'card-color-1',
    'blue':   'card-color-2',
    'pink':   'card-color-3',
    'yellow': 'card-color-4',
    'green':  'card-color-5'
}

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

def color_to_class_name(color: str):
  if color in class_names:
      return class_names[color]
  return None

def color_filter(color: str):
    if color in class_names:
        print(color)
        return color
    print('yellow')
    return 'yellow'
