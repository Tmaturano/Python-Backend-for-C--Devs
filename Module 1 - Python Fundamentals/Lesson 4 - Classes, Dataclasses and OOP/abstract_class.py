# ABC means Abstract Base Class. It is a class that cannot be instantiated and is used to define a common interface for a group of subclasses. 
# In Python, we can create an abstract class by inheriting from the ABC class and using the @abstractmethod decorator to define abstract methods 
# that must be implemented by any subclass.

from abc import ABC 
from abc import abstractmethod

class EmailSender(ABC):

    @abstractmethod
    def send(self):
        pass

class MicrosoftEmailSender(
    EmailSender
):

    def send(self):
        print("Sending")    