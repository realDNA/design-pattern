from state import TrafficLightState


class TrafficLightContext:
    def __init__(self, state: TrafficLightState):
        self._state = state

    def setState(self, state: TrafficLightState):
        self._state = state

    def request(self):
        self._state.handle(self)
