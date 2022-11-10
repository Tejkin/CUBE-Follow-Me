from datetime import datetime
now = datetime.now()
class Event():
    """Event class to record the location, time stamp, presence and motion of an event
    
    Args:
        location (str): takes in the location of the recorded event
        timestamp (datetime): records the time of the event
        presence (bool): detects if someone exists in the current location
        motion (bool): returns if there was motion in the current location
    """

    def __init__(self, location):

        self.location = location
        self.timestamp = now.strftime("%m/%d/%Y - %H:%M:%S")
        self.presence = False
        self.motion = None

    def __str__(self):
        return f"In the {self.location} at {self.timestamp}\tMotion detection is {self.motion}\tPresence is {self.presence}"
    
    def set_motion(self, motion):
        self.motion = motion

    def get_motion(self):
        return self.motion
    
    def set_presence(self):
        if self.motion == True:
            self.presence == True
        else:
            self.presence == False


    
if __name__ == '__main__':
    kitchen = Event("kitchen",)
    kitchen.set_motion(True)

    print(kitchen.__str__())