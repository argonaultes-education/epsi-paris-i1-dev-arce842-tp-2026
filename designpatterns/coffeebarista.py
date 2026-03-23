from abc import ABC, abstractmethod

# milk cost: 0.5
# sugar cost: 0.4

class Beverage(ABC):
    
    def __init__(self):
        self.milk = False
        
        
    def add_milk(self):
        self.milk = True
        
    def add_sugar(self):
        ...
    
    @abstractmethod
    def cost(self):
        ...

# base cost: 1        
class Coffee(Beverage):
    
    def __init__(self):
        super().__init__()
    
    def add_coffee(self):
        ...
    
    def cost(self):
        if self.milk:
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
