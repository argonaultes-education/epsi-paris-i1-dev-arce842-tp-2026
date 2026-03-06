from abc import ABC, abstractmethod

class Beverage(ABC):
    
    def __init__(self):
        ...
        
        
    def add_milk(self):
        ...
        
    def add_sugar(self):
        ...
    
    @abstractmethod
    def cost(self):
        ...
        
class Coffee(Beverage):
    
    def add_coffee(self):
        ...
    
    def cost(self):
        ...    
    
class Tea(Beverage):
    ...
    
class Chocolate(Beverage):
    ...
    
class Latte(Beverage):
    ...
    
