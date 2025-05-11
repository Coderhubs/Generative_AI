from pydantic import BaseModel, EmailStr

import json  # For pretty JSON output


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: list[Address]


user_data = {
    "id": 2,
    "name": "sam",
    "email": "sam@gmail.com",
    "addresses": [
        {
            "street": "123 Main St",
            "city": "New York",
            "zip_code": "10001"
        },
        {
            "street": "456 Elm St",
            "city": "Los Angeles",
            "zip_code": "90001"
        }
    ]
}



user = UserWithAddress.model_validate(user_data)

# Reorder keys manually for pretty output
ordered_data = {
    "id": user.id,
    "name": user.name,
    "email": user.email,
    "addresses": [address.model_dump() for address in user.addresses]
}

print("\nUser data successfully validated and transformed into a model:\n")


print(json.dumps(ordered_data, indent=4))
