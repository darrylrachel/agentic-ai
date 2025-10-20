from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address # Reference of the Address model


address = Address(
    street="123 something",
    city="Bakersfield",
    postal_code="93309"
)

user = User(
    id=1,
    name="Darryl",
    address=address
)


user_data = {
    "id": 1,
    "name": "Darryl",
    "address": {
        "street": "321 something",
        "city": "London",
        "postal_code": "90044"
    }
}

user = User(**user_data)
