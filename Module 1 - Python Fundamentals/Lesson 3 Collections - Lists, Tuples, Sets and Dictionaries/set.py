# Equivalent of HashSet in C#, duplicates are automatically removed

roles: set[str] = {
    "admin",
    "manager",
    "admin"
}

print()
print("Sets:")
print(roles)  # Output: {'admin', 'manager'}


# Check if exists
print(f'"admin" in roles: {"admin" in roles}')  # Output: True