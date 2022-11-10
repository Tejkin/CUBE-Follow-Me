class LocationEvents():
    def __init__(self, location):
        self.location = location
        self.motion = []
    
    def add_event(self, motion):
        if motion == True:
            
