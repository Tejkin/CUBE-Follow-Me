from event import Event
class LocationEvent(Event):
    def __init__(self, location):
        super().__init__(location)
        self.all_motion = []
    
    def add_event(self, location):
        self.all_motion.append(location)















