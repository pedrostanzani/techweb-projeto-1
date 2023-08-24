class Request:
    def __init__(self, raw: str, route: str):
        self.raw = raw
        self.route = route
    
    @classmethod
    def interpret_request(cls, req: str):
        route = cls.extract_route(req)
        if route is None:
            raise Exception("Invalid request format.")
        return cls(req, route)
    
    @staticmethod
    def extract_route(req: str):
        lines = req.splitlines()
        if len(lines) == 0:
            return None
        
        first_line = lines[0]
        path = first_line.split()[1]
        if path[0] == '/':
            path = path[1:]

        return path
