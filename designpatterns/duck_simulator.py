from strategy_duck import Duck, FlyBehavior, QuackBehavior

class DuckSimulator:
    
    def simulate(self, duck : Duck):
        if not isinstance(duck, Duck):
            print('Error, this is not a duck')
            return
        self.__fly_n_times(duck, 2)
        duck.quack() #ERROR: fix this in 2 lines
        self.__fly_n_times(duck, 3)
        
    def __fly_n_times(self, duck : Duck, n_times : int):
        for _ in range(n_times):
            duck.fly()

class Goose:
    
    def honk(self):
        print('Honk honk')
        
    def fly(self):
        print('Fly like a goose')
        
    # def quack(self):
    #     self.honk()

# Adapter
class DuckDisguiseGreen(Duck):

    def __init__(self, goose : Goose):
        super().__init__(None, None)
        self.goose = goose

    def fly(self):
        self.goose.fly()
        
    def quack(self):
        self.goose.honk()

class GooseFly(FlyBehavior):
    
    def __init__(self, goose : Goose):
        self.goose = goose
        
    def fly(self):
        self.goose.fly()
        
class GooseQuack(QuackBehavior):
    
    def __init__(self, goose : Goose):
        self.goose = goose
        
    def quack(self):
        self.goose.honk()

class DuckDisguiseBanana(Duck):
    
    def __init__(self, goose : Goose):
        super().__init__(GooseFly(goose), GooseQuack(goose))

if __name__ == '__main__':
    goose = Goose()
    simulator = DuckSimulator()
    simulator.simulate(DuckDisguiseGreen(goose))
    simulator.simulate(DuckDisguiseBanana(goose))