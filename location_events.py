from event import Event
class LocationEvents():
    def __init__(self):
        self.all_motion = []
    
    def add_event(self, location):
        self.all_motion.append(location)