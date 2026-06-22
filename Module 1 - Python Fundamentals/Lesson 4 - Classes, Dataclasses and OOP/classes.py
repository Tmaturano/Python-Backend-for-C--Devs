# self is like "this" in C#

# self.name is equivalent to public string Name { get; set; } in C#

class User:

    def __init__(self, name: str):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")        

user = User("Thiago")

print(user.name)    
user.greet()    