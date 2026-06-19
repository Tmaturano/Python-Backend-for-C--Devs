user: dict[str, str | int] = {
    "id": 1,
    "name": "Thiago",
    "email": "thiago@email.com"
}

print(user["name"])  # Output: Thiago

# Adding a new key-value pair
user["role"] = "Developer"

print(user)  # Output: {'id': 1, 'name': 'Thiago', 'email': 'thiago@email.com', 'role': 'Developer'}

# Removing a key-value pair
del user["email"]
print(user)  # Output: {'id': 1, 'name': 'Thiago', 'role': 'Developer'}

# Check if a key exists
print(f'"name" in user: {"name" in user}')  # Output: True

# Get a value with a default if the key doesn't exist
print(user.get("email", "Not found"))  # Output: Not found

# Otherwise, will return "None"
print(user.get("email"))  # Output: None


# Looping through a dictionary
print()
for key, value in user.items():
    print(key, value)


# Real backend example:
response = {
    "id": 1,
    "name": "Thiago",
    "roles": [
        "admin",
        "developer"
    ]
}

print()
roles = response["roles"]
print(roles)  # Output: ['admin', 'developer']

if ("admin" in roles):
    print("Allowed")