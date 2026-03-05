from abc import ABC, abstractmethod

class Duck(ABC):
    
    @abstractmethod
    def display(self):
        ...
        
    @abstractmethod
    def fly(self):
        ...
    
class GreenDuck(Duck):
    
    def display(self):
        print('Greenduck says hello')
        
    def fly(self):
        print('Fly to the moon')
    
    def quack(self):
        print('Quack quack')
    
class MallardDuck(Duck):

    def display(self):
        print('MallardDuck says hello')
        
    def fly(self):
        print('Fly to the moon')
    
    def quack(self):
        print('Small quack')
