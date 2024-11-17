from state import TrafficLightState


class RedLightState(TrafficLightState):
    def handle(self, context):
        print("Red Light: Stop")
        context.setState(GreenLightState())


class GreenLightState(TrafficLightState):
    def handle(self, context):
        print("Green Light: Go")
        context.setState(YellowLightState())


class YellowLightState(TrafficLightState):
    def handle(self, context):
        print("Yellow Light: Caution")
        context.setState(RedLightState())
