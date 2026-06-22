try:
    int("abc")
except Exception as ex:
    print(ex)
    #raise # re-raise the exception to propagate it up the call stack, equivalent to throw in C#


# Multiple except blocks:
try:
    ...
except ValueError:
    ...
except KeyError:
    ...
except Exception:
    ...    

# Finally block:
try:
    print("Working")
finally:
    print("Cleanup")#     


# Raising exceptions:
#raise Exception("Something went wrong")
#raise ValueError("Invalid user id")


# Custom exceptions:
class InvalidUserIdException(Exception):
    pass

#raise InvalidUserIdException("Invalid user id")