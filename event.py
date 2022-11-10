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
        """
        Returns arguments in an appropriate, readable format
        """
        return f"In the {self.location} at {self.timestamp}\nMotion detection is {self.motion}\nPresence is {self.presence}"
    
    def set_motion(self, motion):
        """
        Motion parameter setter and also sets presence accordingly

        Args:
            motion (bool): motion detector response

        Return
            presence (bool): true if motion is true, false if motion is false
        """
        self.motion = motion
        if motion == True:
            self.presence = True
        else:
            self.presence = False

    def get_motion(self):
        """
        Motion getter

        Return:
            motion (bool): motion detector response
        """
        return self.motion

    def get_presence(self):
        """
        Presence getter

        Return:
            presence(bool): dependent on motion parameter
        """
        return self.presence

    
if __name__ == '__main__':
    kitchen = Event("kitchen",)
    kitchen.set_motion(True)

    bedroom = Event("bedroom")
    bedroom.set_motion(False)

    print(kitchen.__str__())
    print(bedroom.__str__())
    pass