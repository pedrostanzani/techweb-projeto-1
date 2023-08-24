class Request:
    def __init__(self, raw: str, route: str, method: str):
        self.raw = raw
        self.route = route
        self.method = method

    def log(self):
        print(self.raw)
    
    @classmethod
    def interpret_request(cls, req: str):
        method, route = cls.extract_metadata(req)
        if route is None:
            raise Exception("Invalid request format.")
        return cls(req, route, method)
    
    @staticmethod
    def extract_metadata(req: str):
        lines = req.splitlines()
        if len(lines) == 0:
            return None
        
        first_line = lines[0]
        method, path = first_line.split()[0:2]
        if path[0] == '/':
            path = path[1:]

        return method, path
