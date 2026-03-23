from abc import ABC, abstractmethod

# milk cost: 0.5
# sugar cost: 0.4

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

# base cost: 1        
class Coffee(Beverage):
    
    def add_coffee(self):
        ...
    
    def cost(self):
        ...    

# base cost: 1.5    
class Tea(Beverage):
    ...
    
# base cost: 0.7
class Chocolate(Beverage):
    ...

# base cost: 2.0    
class Latte(Beverage):
    ...
    
    
if __name__ == '__main__':
    c = Coffee()
    print(c.cost())
    c.add_sugar()
    print(c.cost())
    tea = Tea()
    tea.add_milk()
    print(tea.cost())
