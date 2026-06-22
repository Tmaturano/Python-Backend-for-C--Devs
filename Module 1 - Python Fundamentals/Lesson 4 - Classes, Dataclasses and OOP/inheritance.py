class Animal:

    def speak(self):
        print("...")

class Dog(Animal):

    def speak(self):
        print("Woof")        

dog = Dog()

dog.speak() # Output: Woof