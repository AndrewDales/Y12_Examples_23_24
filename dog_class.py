class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Runs on initialisation of any instance
    def __init__(self, name, age):
        # name and age are attributes for each instance of the class
        self.name = name
        self.age = age

    # Method - something that the class instance does.
    def speak(self, sound):
        return f'{self.name} says {sound}!'

    # 'dunder' function to change how object is printed out.
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"


class JackRussell(Dog):
    def speak(self):
        return super().speak(sound='arf')


if __name__ == "__main__":
    my_dog = Dog('Fido', 5)
