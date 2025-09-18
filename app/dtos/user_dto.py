from ninja import Schema

class UserIn(Schema):
    name: str
    email: str

class UserOut(Schema):
    id: int
    name: str
    email: str
