## Animal is- a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Is A
class Dog(Animal):

    def __init__(self, name):
        ##  Has A
        self.name = name  

## Is A
class Person(object):
    def __init__(self, name):
        ## Has A
        self.name = name

        ## Has-A
        self.pet = None

## Is A
class Employee(Person):
    def __init__(self, name, salary):
        ## Has A
        super(Employee, self).__init__(name)
        ## Has A
        self.salary = salary

## Is A
class Fish(object):
    pass

## Is A
class Salmon(Fish):
     pass                   

## Is A
class Halibut(Fish):
     pass


## rover is- a Dog
rover = Dog("Rover")

## Is A 
satan = Cat("Satan")

## is A
mary = Person("Mary")

## pet attribute of mary is-a sat
mary.pet = satan

## pet attribute of frank is-a rover
frank = Employee("Frank", 120000)

## Has A
frank.pet = rover

## Is A
flipper = Fish()

## Is A
crouse = Salmon()

## Is A
harry = Halibut()
     
