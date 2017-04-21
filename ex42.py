## Animal is-a object (yes, sort of conusing) look at the extra credit
class Animal(object):
    pass

# is-a
class Dog(Animal):

    def __init__(self, name):
        # has-a
        self.name = name

# is-a
class Cat(Animal):

    def __init__(self, name):
        # has-a
        self.name

# has-a
class Person(object):

    def __init__(self, name):
        # is-a
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

# is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        # has-a
        self.salary = salary

#has-a
class Fish(object):
    pass

# is-a
class Salmon(Fish):
    pass

# has-a
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

# is-a
satan = Cat("Satan")

# is-a
mary = Person("Mary")

# has-a
mary.pet = Satan

# is-a
frank = Employee("Frank", 120000)

# has-a
frank.pet = rover

# ?
flipper = fish()

# ?
crouse = Salmon()

# ?
harry = Halibut()
