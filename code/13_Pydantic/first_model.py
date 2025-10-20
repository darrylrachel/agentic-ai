from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    'id': 101,
    'name': "Blackheart Labs",
    'is_active': True,
}

# user object
# ** unpacks input_data
user = User(**input_data)
print(user)