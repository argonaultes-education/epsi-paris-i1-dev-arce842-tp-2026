from abc import ABC, abstractmethod, abstractclassmethod

class QuackBehavior(ABC):
    
    @abstractmethod
    def quack(self):
        ...

class QuackQuack(QuackBehavior):
    
    def quack(self):
        print('Quack quack')
        
class SmallQuack(QuackBehavior):
    
    def quack(self):
        print('Small quack')

class FlyBehavior(ABC):
    
    @abstractclassmethod
    def fly(self):
        ...

class FlyToTheMoon(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Fly to the moon')

class FlyBackward(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Backward flying')


class Duck(ABC):
    
    def __init__(self, fly_behavior:FlyBehavior, quack_behavior:QuackBehavior):
        self.__fly_behavior = fly_behavior
        self.__quack_behavior = quack_behavior
    
    def display(self):
        print(self.__class__.__name__, 'says hello')
    
    def set_fly_behavior(self, fly_behavior:FlyBehavior):
        self.__fly_behavior = fly_behavior
    
    def fly(self):
        self.__fly_behavior.fly()
        
    def set_quack_behavior(self, quack_behavior:QuackBehavior):
        self.__quack_behavior = quack_behavior
        
    def quack(self):
        self.__quack_behavior.quack()

    
class GreenDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=QuackQuack())
    
class MallardDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyBackward, quack_behavior=SmallQuack())

class OtherDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=SmallQuack())

if __name__ == '__main__':
    green_duck = GreenDuck()
    green_duck.display()
    green_duck.fly()
    green_duck.quack()
    green_duck.set_fly_behavior(FlyBackward)
    green_duck.fly()

    
    mallard = MallardDuck()
    mallard.display()
    mallard.fly()
    mallard.quack()
    mallard.set_quack_behavior(QuackQuack())
    mallard.quack()