class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
        print(self.name, self.pet)

class Employee(Person):

    def __init__(self, name, salary):
        self.name = name
        super(Employee, self).__init__(name)
        self.salary = salary
        print(self.name, self.salary)

Mary = Person("Mary")

John = Employee("John", 35000)
