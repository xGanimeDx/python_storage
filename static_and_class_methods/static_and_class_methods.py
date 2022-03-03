from tokenize import PseudoExtras


class person():
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this is a class method
    # provide a possibility to call this method without creating an object of the class, see below
    # cls is a mandatory attribute for such methods
    # also class methods should be marked with @classmethod
    @classmethod
    def getPopulation(cls):
        return cls.population

    # this is a static method
    # provide a possibility to call this method without creating an object of the class, see below
    # there are no mandatory attributes for static methods
    # also static methods should be marked with @staticmethod
    @staticmethod
    def isAdult(age):
        return age >= 18

    # this is regular method
    # self is a mandatory parameter for such methods
    def display(self):
        print(self.name, "is", self.age, "years old")

human = person("stan", 15)

# example of using class method directly from the class
print(person.getPopulation())

# example of using static method directly from the class
print(person.isAdult(18))