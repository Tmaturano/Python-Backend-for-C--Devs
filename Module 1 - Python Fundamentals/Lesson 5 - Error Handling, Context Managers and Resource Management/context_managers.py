# One of the most important concepts in Python is the idea of a context manager. 
# A context manager is a way to manage resources, such as files, network connections, 
# or database connections, in a way that ensures that they are properly cleaned up after use.

from pathlib import Path

# Pythonic Style:
# 'with ...' Python automatically closes the file
# it's like using(var file = ...), IDisposable in C#
file_path = Path(__file__).with_name("file.txt") # file_path is the same as Path("file.txt") because it's in the same directory as the script
with file_path.open(encoding="utf-8") as file:
    data = file.read()
    print(data)



# Resource Management in APIs    

# Files: with open(...)
# SQLAlchemy Sessions: with Session(...)
# Transactions: with session.begin():
# Locks: with lock: