from routes import index
from utils import read_file, build_response
from request import Request
from pathlib import Path

CUR_DIR = Path(__file__).parent

def handle_request(request: Request):
    route = request.route
    filepath = CUR_DIR / route
    if filepath.is_file():
        if str(filepath).endswith(".svg"):
            response = build_response(headers="Content-Type: image/svg+xml") + read_file(filepath)
        else:
            response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    else:
        response = build_response(code=404)

    return response
