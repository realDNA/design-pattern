from context import TrafficLightContext
from concreteState import RedLightState

trafficLight = TrafficLightContext(RedLightState())

trafficLight.request()
trafficLight.request()
trafficLight.request()
trafficLight.request()
