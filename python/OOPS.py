# Inheritance in Python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # Call the constructor of the Parent class to initialize the name attribute
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

class GrandChild(Child):
    def __init__(self, name, age, hobby):
        super().__init__(name, age) # Call the constructor of the Child class to initialize the name and age attributes
        self.hobby = hobby

    def share_hobby(self):
        print(f"My hobby is {self.hobby}.")

# Create an instance of the Child class
child = Child("Alice", 10)
child.greet()  # Calls the greet method from the Parent class
child.introduce()  # Calls the introduce method from the Child class   

grandchild = GrandChild("Bob", 5, "drawing")
grandchild.greet()  # Calls the greet method from the Parent class
grandchild.introduce()  # Calls the introduce method from the Child class
grandchild.share_hobby()  # Calls the share_hobby method from the GrandChild class

# Polymorphism in Python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")      

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the speak method on each instance Method overriding allows the Dog and Cat classes to provide their own implementation of the speak method, which is defined in the Animal class. This is an example of polymorphism, where the same method name can have different behaviors based on the object that calls it.
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!

# Overloading in Python
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):  # Method overloading is not directly supported in Python, but we can achieve similar behavior using default arguments.
        return a + b + c

# Create an instance of MathOperations
math = MathOperations()

# Call the add method with different numbers of arguments
print(math.add(2, 3))  # Output: 5
print(math.add(2, 3, 4))  # Output: 9


# Abstract Classes in Python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementing the abstract method.")

# Create an instance of the concrete class
obj = ConcreteClass()
obj.abstract_method()  # Output: Implementing the abstract method.

# Encapsulation in Python Encapsulation is the concept of restricting access to certain attributes and methods of an object, which can help prevent unintended interference and misuse of the object's internal state. In Python, encapsulation is typically achieved using private attributes and methods, which are indicated by a double underscore prefix (e.g., __private_attribute).
class EncapsulatedClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value        

