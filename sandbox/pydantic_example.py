from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive',default=False)
    addresses: Address



user = User(id=1, name='Alice', email='alice@example.com',addresses= Address(city='New York', zip_code='9410'))
print(user.model_dump_json())


