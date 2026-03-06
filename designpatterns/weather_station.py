import random
import datetime
from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def notify(self, weather_station):
        ...
    

class StatsDisplay(Observer):
    
    def notify(self, weather_station):
        print(f'{weather_station.temperature} | {weather_station.pressure} | {weather_station.humidity}')
        
class AverageTempDisplay(Observer):
    
    def __init__(self):
        self.__accu_temp = 0
        self.__nb_temp = 0
    
    def average_temp(self, temperature):
        self.__accu_temp += temperature
        self.__nb_temp += 1
        print(f'avg temp {self.__accu_temp / self.__nb_temp}')
        
    def notify(self, weather_station):
        self.average_temp(weather_station.temperature)

class MaxPressureDisplay(Observer):
    
    def __init__(self):
        self.__max_pressure = 0
        
    def notify(self, weather_station):
        pressure = weather_station.pressure
        if self.__max_pressure < pressure:
            self.__max_pressure = pressure
        print(f'Max pressure: {self.__max_pressure}')

class WeatherStation:
    
    def __init__(self):
        self.__displays = []
        
    def add_display(self, display:Observer):
        if isinstance(display, Observer):
            self.__displays.append(display)
    
    def __get_temperature(self):
        return random.randint(-50, 50)
    
    def __get_pressure(self):
        return random.randint(800, 1200)
    
    def __get_humidity(self):
        return random.randint(0, 100)
    
    def __get_pm(self):
        return random.randint(0, 1000)
    
    @property
    def temperature(self):
        return self.__current_temp
    
    @property
    def pressure(self):
        return self.__current_pressure

    @property
    def humidity(self):
        return self.__current_humidity

    @property
    def pm(self):
        return self.__current_pm

    
    def update_measures(self):
        self.__current_temp = self.__get_temperature()
        self.__current_pressure = self.__get_pressure()
        self.__current_humidity = self.__get_humidity()
        self.__current_pm = self.__get_pm()

        for display in self.__displays:
            display.notify(self)
        
if __name__ == '__main__':
    weather_station = WeatherStation()
    weather_station.add_display(StatsDisplay())
    weather_station.add_display(AverageTempDisplay())
    weather_station.add_display(MaxPressureDisplay())
    
    for _ in range(1):
        print(datetime.datetime.now())
        weather_station.update_measures()