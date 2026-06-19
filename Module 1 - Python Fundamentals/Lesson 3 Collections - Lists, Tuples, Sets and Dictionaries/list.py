names: list[str] = [
    "Thiago",
    "John",
    "Maria"
]

print(names[0])  # Output: Thiago

names.append("Alice")
print(names)  # Output: ['Thiago', 'John', 'Maria', 'Alice']

names.remove("John")
print(names)  # Output: ['Thiago', 'Maria', 'Alice']

print(len(names))  # Output: 3

# ----------

# Looping through a list
for name in names:
    print(name)

# ----------

# Python superpowers: List comprehensions
print()
numbers: list[int] = [1, 2, 3, 4, 5]
squared_numbers: list[int] = [num ** 2 for num in numbers]
print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]    
doubled: list[int] = [n * 2 for n in numbers]
print(f"Doubled numbers: {doubled}")  # Output: [2, 4, 6, 8, 10]


# ----------

# Filtering
print()
numbers: list[int] = [1, 2, 3, 4, 5]

evens: list[int] = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")  # Output: [2, 4]
