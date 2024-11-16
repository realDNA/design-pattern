from observer import Observer


class CurrentConditionDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(
            f"Current condition: temperature: {temperature} C, humidity: {humidity} %, {pressure} hpa")


class StaticDisplay(Observer):
    def __init__(self):
        self.temperatures = []
        self.humidities = []
        self.pressures = []

    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)
        avgTemp = sum(self.temperatures) / len(self.temperatures)
        avgHumidity = sum(self.humidities) / len(self.humidities)
        avgPressure = sum(self.pressures) / len(self.pressures)
        print(
            f"average temperature: {avgTemp} C, average humidity: {avgHumidity} %, average pressure: {avgPressure} hpa")
