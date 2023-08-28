import routes

from utils import read_file, build_response
from request import Request
from pathlib import Path

CUR_DIR = Path(__file__).parent

def handle_request(request: Request):
    route = request.route
    filepath = CUR_DIR / route

    print("ROUTE >>", route)

    # Static file handling
    if filepath.is_file():
        if str(filepath).endswith(".svg"):
            response = build_response(headers="Content-Type: image/svg+xml") + read_file(filepath)
        else:
            response = build_response() + read_file(filepath)
            
    # @route : /
    elif route == '':
        response = routes.index(request)

    # @route : /api/notes
    elif route.startswith('api/notes'):
        paths = route.split('/')
        if paths != 3:
            response = build_response(code=400)
        note_id = paths[-1]
        if not note_id.isdigit():
            response = build_response(code=400)
        response = routes.notes(request, note_id)

    elif route.startswith('editar'):
        paths = route.split('/')
        if paths != 2:
            response = build_response(code=400)
        note_id = paths[-1]
        if not note_id.isdigit():
            response = build_response(code=400)
        response = routes.edit_note(request, note_id)

    else:
        response = build_response(code=404)

    return response
