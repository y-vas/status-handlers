from .base import HTTPException

class E401(HTTPException):
    def __init__(self):
        self.status_code = 401
        self.detail = "This resource requires proper authorization!"
        self.headers = None

class E403(HTTPException):
    def __init__(self):
        self.status_code = 403
        self.detail = 'This action is forbiden!'
        self.headers = None

class E404(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = 'Resource not found!'
        self.headers = None

class E409(HTTPException):
    def __init__(self):
        self.status_code = 409
        self.detail = 'This action is causes undocumented conflicts!'
        self.headers = None

class E409_1(HTTPException):
    def __init__(self, entity:str = 'resource' ):
        self.status_code = 409.01
        self.detail = f'Conflict, this {entity} already exists!'
        self.headers = None

class E409_2(HTTPException):
    def __init__(self):
        self.status_code = 409.02
        self.detail = 'Conflict, this resource has reached max amount!'
        self.headers = None

class E429(HTTPException):
    def __init__(self):
        self.status_code = 429
        self.detail = 'Rate limit exceded for this resource!'
        self.headers = None
