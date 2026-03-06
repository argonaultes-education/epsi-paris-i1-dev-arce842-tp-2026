import random
import datetime

class StatsDisplay:
    
    def display(self, temperature, pressure, humidity):
        print(f'{temperature} | {pressure} | {humidity}')
        
class AverageTempDisplay:
    
    def __init__(self):
        self.__accu_temp = 0
        self.__nb_temp = 0
    
    def average_temp(self, temperature):
        self.__accu_temp += temperature
        self.__nb_temp += 1
        print(f'avg temp {self.__accu_temp / self.__nb_temp}')

class WeatherStation:
    
    def __init__(self, stats_display:StatsDisplay, average_temp_display:AverageTempDisplay):
        self.__stats_display = stats_display
        self.__avg_temp_display = average_temp_display
    
    def get_temperature(self):
        return random.randint(-50, 50)
    
    def get_pressure(self):
        return random.randint(800, 1200)
    
    def get_humidity(self):
        return random.randint(0, 100)
    
    def update_measures(self):
        current_temp = self.get_temperature()
        current_pressure = self.get_pressure()
        current_humidity = self.get_humidity()
        
        self.__stats_display.display(current_temp, current_pressure, current_humidity)
        self.__avg_temp_display.average_temp(current_temp)
        
if __name__ == '__main__':
    weather_station = WeatherStation(StatsDisplay(), AverageTempDisplay())
    
    for _ in range(10):
        print(datetime.datetime.now())
        weather_station.update_measures()