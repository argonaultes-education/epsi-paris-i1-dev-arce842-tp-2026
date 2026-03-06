import random
import datetime
from abc import ABC, abstractmethod

class AbstractDisplay(ABC):
    
    @abstractmethod
    def display(self, temperature, pressure, humidy):
        ...
    

class StatsDisplay(AbstractDisplay):
    
    def display(self, temperature, pressure, humidity):
        print(f'{temperature} | {pressure} | {humidity}')
        
class AverageTempDisplay(AbstractDisplay):
    
    def __init__(self):
        self.__accu_temp = 0
        self.__nb_temp = 0
    
    def average_temp(self, temperature):
        self.__accu_temp += temperature
        self.__nb_temp += 1
        print(f'avg temp {self.__accu_temp / self.__nb_temp}')
        
    def display(self, temperature, pressure, humidity):
        self.average_temp(temperature)

class MaxPressureDisplay(AbstractDisplay):
    
    def __init__(self):
        self.__max_pressure = 0
        
    def display(self, temperature, pressure, humidity):
        if self.__max_pressure < pressure:
            self.__max_pressure = pressure
        print(f'Max pressure: {self.__max_pressure}')

class WeatherStation:
    
    def __init__(self):
        self.__displays = []
        
    def add_display(self, display:AbstractDisplay):
        if isinstance(display, AbstractDisplay):
            self.__displays.append(display)
    
    def get_temperature(self):
        return random.randint(-50, 50)
    
    def get_pressure(self):
        return random.randint(800, 1200)
    
    def get_humidity(self):
        return random.randint(0, 100)
    
    def get_pm(self):
        return random.randint(0, 1000)
    
    def update_measures(self):
        current_temp = self.get_temperature()
        current_pressure = self.get_pressure()
        current_humidity = self.get_humidity()

        for display in self.__displays:
            display.display(current_temp, current_pressure, current_humidity)
        
if __name__ == '__main__':
    weather_station = WeatherStation()
    weather_station.add_display(StatsDisplay())
    weather_station.add_display(AverageTempDisplay())
    weather_station.add_display(MaxPressureDisplay())
    
    for _ in range(10):
        print(datetime.datetime.now())
        weather_station.update_measures()