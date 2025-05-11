from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field


""" age: int | None = None → Optional field:
Can be an integer.
Can be None (missing).
Has default value None
"""

user_data = {
    "id": 1,
    "name": "Aayat",
    "email": "Aayatjabbar@gmail.com",
    "age": 22
}

user = User(**user_data)  # unpacking the dictionary using **

# Clean output
print(f"\nUser Object:\n\n{user}\n")

# Convert to dictionary
print(f"\nUser as Dictionary:\n\n{user.model_dump()}\n")

# Now testing invalid data
try:
    invalid_user = User(id="not_an_integer", name="Bob", email="bob@example.com")

except ValidationError as e:
    print("\nValidation Error Encountered:\n")
    print(f"Error Details:\n\n{e}\n")
    # The error message is printed cleanly with extra formatting
