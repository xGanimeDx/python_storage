class person():
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    @staticmethod
    def isAdult(age):
        return age >= 18

    @classmethod
    def getPopulation(cls):
        return cls.population