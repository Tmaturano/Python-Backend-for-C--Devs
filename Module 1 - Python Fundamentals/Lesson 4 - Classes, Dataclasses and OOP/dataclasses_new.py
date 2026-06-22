# This is where moderns Python differs from older Python. 
# We can use dataclasses to avoid writing boilerplate code for classes that are mainly used to store data.
#Why Dataclasses?

#Python generates:

#Constructor
#Equality
#String representation

# Instead of:
class User:

    def __init__(
        self,
        id: int,
        name: str
    ):
        self.id = id
        self.name = name

# We can use dataclasses: which looks like record types in C# 9.0 and above
from dataclasses import dataclass

@dataclass  #mutable dataclass
class User:
    id: int
    name: str        

# usage:
user = User(
    id=1,
    name="Thiago"
)    

print(user) # Output: User(id=1, name='Thiago')
user.name = "John"
print(user) # Output: User(id=1, name='John')


# To make it immutable, we can use frozen=True:
@dataclass(frozen=True)  #immutable dataclass
class ImmutableUser:
    id: int
    name: str
    
immutableUser = ImmutableUser(
    id=1,    
    name="Thiago"
)
# immutableUser.name = "John" # This will raise a dataclasses.FrozenInstanceError: cannot assign to field 'name'

# Equality:

user1 = User(1, "Thiago")
user2 = User(1, "Thiago")

print(f"Equality: user1 == user2: {user1 == user2}") # Output: True
