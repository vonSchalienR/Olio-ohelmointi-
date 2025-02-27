class WeatherStation:
    def __init__(self, name):
        self.__name = name  # atribuutti
        self.__observations = []  # lista
    
    def add_observation(self, observation: str):
        self.__observations.append(observation)  # lisää havainnon listaan
    
    def latest_observation(self):
        if self.__observations:
            return self.__observations[-1]  # palauttaa viimeisimmän havainnon
        return ""  
    
    def number_of_observations(self):
        return len(self.__observations)  # palauttaa havaintojen lukumäärän
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations" 

# Test the implementation
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation()) 
station.add_observation("Thunderstorm")
print(station.latest_observation()) 
print(station.number_of_observations())  
print(station)  
