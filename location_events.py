from event import Event
class LocationEvent(Event):
    def __init__(self, location):
        super().__init__(location)
        self.all_motion = []
    
    def add_event(self, location, past_presence, current_presence):
        self.all_motion.append(f'The room is the {location}, it\'s presence changed from {past_presence} to {current_presence}')















