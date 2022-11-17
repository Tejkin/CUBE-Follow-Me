from event import Event
class LocationEvent(Event):
    def __init__(self, location):
        super().__init__(location)
        self.all_motion = []
    
    def add_event(self, location, past_presence, current_presence):
        """
        Appends all changes in motion to all_motion list

        Args:
            location(string): the current location
            past_presence(bool): the previous presence value
            current_presence(bool): the current presence value

        Return:
            appends all_motion list in string format
        """
        self.all_motion.append(f'The room is the {location}, it\'s presence changed from {past_presence} to {current_presence}')















