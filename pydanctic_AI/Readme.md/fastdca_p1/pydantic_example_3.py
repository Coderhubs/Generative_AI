from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class userwithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_contain_at_least_3_characters(cls, value):
        if len(value) < 3:
            raise ValueError("Dear user Name must contain at least 3 characters")
        return value

    @validator("email")
    def email_must_contain_gmail(cls, value):
        if "gmail.com" not in value:
            raise ValueError("Dear user Email must contain gmail")
        return value

try:
    invalid_user = userwithAddress(
        id=3,
        name="sa",
        email="charlie@yahoo.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}]
    )

except ValidationError as e:
    # Cleanly print out the errors


    print("\nValidation errors:\n")
    for error in e.errors():
        field = error['loc'][0]  # Field name (e.g., 'name', 'email')
        message = error['msg']  # Error message
        print(f"Field: {field}, Error: {message}")
