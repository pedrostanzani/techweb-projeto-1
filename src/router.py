from request import Request

def handle_request(request: Request, current_directory=None):
    if current_directory is None:
        raise Exception("Please provide a source directory for file management.")
    pass
