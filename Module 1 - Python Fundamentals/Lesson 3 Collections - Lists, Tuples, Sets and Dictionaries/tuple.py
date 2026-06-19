# Tuples (Immutable collections)
user: tuple[int, str] = (1, "Thiago")
print()
print("Tuples:")
print(user[0])  # Output: 1
print(user[1])  # Output: Thiago


# ----------

def get_user() -> tuple[int, str]:
    return 1, "Thiago"

id, name = get_user()

print(f"ID: {id}, Name: {name}")  # Output: ID: 1, Name: Thiago