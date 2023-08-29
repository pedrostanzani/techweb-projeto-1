from urllib.parse import unquote_plus


class Request:
    def __init__(self, raw: str, route: str, method: str):
        self.raw = raw
        self.route = route
        self.method = method

    def log(self):
        print(self.raw)

    def get_query_params(self):
        raw_request = self.raw.replace('\r', '')
        partes = raw_request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[unquote_plus(chave)] = unquote_plus(valor)

        return params
    
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
