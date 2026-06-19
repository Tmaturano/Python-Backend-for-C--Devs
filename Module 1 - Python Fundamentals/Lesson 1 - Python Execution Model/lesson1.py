print("Program started")

# Python infers the type of variables by default
first = "Thiago"
last = "Maturana"

full_name = f"{first} {last}"

# In modern python, prefer to use type hints
age: int = 36

print(f"Hello {full_name}, you are {age} years old.")