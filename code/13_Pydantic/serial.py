from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-Y %H:%M:%S")}
    )

user = User(
    id=1,
    name="Darryl",
    email="racheldarryl@ai.com",
    created_at=datetime(2025, 10, 20, 12, 25),
    address=Address(
        street="123 somwhere",
        city="Bakersfield",
        zip_code="93309"
    ),
    is_active=False,
    tags=["Premium", "Subscriber"]
)

python_dict = user.model_dump()

print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)