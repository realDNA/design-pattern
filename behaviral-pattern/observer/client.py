from concreteSubject import WeatherData
from concreteObserver import CurrentConditionDisplay, StaticDisplay


weatherData = WeatherData()

currentDisplay = CurrentConditionDisplay()
statisticsDisplay = StaticDisplay()

weatherData.attach(currentDisplay)
weatherData.attach(statisticsDisplay)

weatherData.setMeasurement(temperature=27, humidity=65, pressure=1012)
weatherData.setMeasurement(temperature=26, humidity=64, pressure=1011)
weatherData.setMeasurement(temperature=25, humidity=63, pressure=1010)
