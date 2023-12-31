from database import Database, Note

from html import escape
from utils import load_template, build_response, color_to_class_name, color_filter

db = Database('database')


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.method == 'POST':
        params = request.get_query_params()
        db.add(Note(title=params['titulo'], content=params['detalhes'], color=color_filter(params['color'])))
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=escape(note_object.title), details=escape(
            note_object.content), note_id=note_object.id, color=color_to_class_name(note_object.color))
        for note_object in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    response_body = load_template('index.html').format(notes=notes)
    response = build_response(body=response_body)
    return response


def notes(request, note_id):
    if request.method == 'DELETE':
        note_id = int(note_id)
        db.delete(note_id)
        return build_response(code=204)

    if request.method == 'GET':
        note_id = int(note_id)
        note = db.get(note_id)
        if not note:
            return build_response(code=404)
        return build_response(code=200, body=note.to_json(), headers="Content-Type: application/json")

    return build_response(code=405)


def edit_note(request, note_id):
    if request.method == 'GET':
        response_body = load_template('edit.html').format(note_id=note_id)
        response = build_response(body=response_body)
        return response

    if request.method == 'POST':
        params = request.get_query_params()
        db.update(Note(title=params['titulo'],
                  content=params['detalhes'], color=color_filter(params['color']), id=note_id))
        return build_response(code=303, reason='See Other', headers='Location: /')

    return build_response(code=405)


def error():
    response_body = load_template('404.html')
    response = build_response(body=response_body)
    return response
