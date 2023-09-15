

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal is making a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak() method for each instance
print("A dog will:") 
dog.speak()
print("A Cat will:")
cat.speak()

