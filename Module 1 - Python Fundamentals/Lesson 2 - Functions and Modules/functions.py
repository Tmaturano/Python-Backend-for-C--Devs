def add(a: int, b: int) -> int:
    return a + b

# Equivalent to the above function in C#
#public int Add(int a, int b)
#{
#    return a + b;
#}


# You can assign functions to variables in Python
def greet():
    print("Hello")

say_hi = greet

say_hi()

# ----------

# Optional Parameters

# In C#, you have:
# void Log(string message = "")

def log(message: str = ""):
    print(message)

log()
log("Optional Parameters")    


# ----------

# Named Arguments
def create_user(
    name: str,
    age: int,
    email: str
):
    pass

# call:
create_user(
    name="Thiago",
    age=36,
    email="thiago@email.com"
)


# ----------

# Return Multiple Values  (Similar to Tuples in C#)
def get_person():
    return "Return Multiple Values: Thiago", 36


name, age = get_person()

print()
print(f"name: {name}")
print(f"age: {age}")


# ----------

# Variable Number of Parameters
def sum_numbers(*numbers: int) -> int:
    return sum(numbers)

print()
print("Variable Number of Parameters:")
print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5))     # Output: 9


