import routes

from utils import read_file, build_response, load_template
from request import Request
from pathlib import Path

CUR_DIR = Path(__file__).parent

def handle_request(request: Request):
    route = request.route
    filepath = CUR_DIR / route

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
        if route.endswith('/'):
            route = route[:-1]
        paths = route.split('/')

        if len(paths) != 3:
            return build_response(code=400)
            
        note_id = paths[-1]
        if not note_id.isdigit():
            return build_response(code=400)
        
        response = routes.notes(request, note_id)

    elif route.startswith('editar'):
        paths = route.split('/')
        if paths[0] != 'editar':
            return routes.error()
        if len(paths) != 2:
            return build_response(code=400)
        note_id = paths[-1]
        if not note_id.isdigit():
            return build_response(code=400)
        response = routes.edit_note(request, note_id)

    else:
        response = routes.error()

    return response
