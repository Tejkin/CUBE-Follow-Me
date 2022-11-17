from datetime import datetime
now = datetime.now()

class Event():
    """
    Event class to record the location, time stamp, presence and motion of an event
    
    Args:
        location (str): takes in the location of the recorded event
        timestamp (datetime): records the time of the event
        presence (bool): detects if someone exists in the current location
        motion (bool): returns if there was motion in the current location
    """

    def __init__(self, location):

        self.__location = location
        self.__timestamp = now.strftime("%m/%d/%Y - %H:%M:%S")
        self.__presence = False
        self.__past_presence = False
        self.__motion = None
        self.all_locations = []

    def __str__(self):
        """
        Returns arguments in an appropriate, readable format
        """
        return f"In the {self.__location} at {self.__timestamp}\nMotion detection is {self.__motion}\nPresence is {self.__presence}"
    
    def set_motion(self, motion):
        """
        Motion parameter setter and also sets presence accordingly

        Args:
            motion (bool): motion detector response

        Return
            presence (bool): true if motion is true, false if motion is false
        """
        self.__motion = motion
        if motion == True:
            self.set_presence(True)
        else:
            return


    def get_motion(self):
        """
        Motion getter

        Return:
            motion (bool): motion detector response
        """
        return self.__motion

    def get_presence(self):
        """
        Presence getter

        Return:
            presence(bool): dependent on motion parameter
        """
        return self.__presence

    def set_presence(self, presence):
        """
        Presence setter
        Also runs set_past_presence() command to store past presence

        Args:
            presence (bool): presence the user would like to change to

        
        """
        self.set_past_presence()
        self.__presence = presence

    def get_location(self):
        """
        Location getter

        Return:
            location(string): returns the location of the current event
        """
        return self.__location

    def set_past_presence(self):
        """
        Past presence setter

        Stores current presence as past presence
        """
        self.__past_presence = self.__presence
        

    def get_past_presence(self):
        """
        Past presence getter

        Returns:
            past presence(bool): returns the previously stored presence
        """
        return self.__past_presence

    def check_presence_change(self):
        """
        Checks if presence has changed

        Returns:
            change(bool): if current presence = previous presence: returns False, otherwise returns true
        """
        if self.get_past_presence() == self.__presence:
            return False
        else:
            return True


if __name__ == '__main__':
    kitchen = Event("kitchen",)
    kitchen.set_motion(True)

    bedroom = Event("bedroom")
    bedroom.set_motion(False)

    print(kitchen)
    print(bedroom)
    print(kitchen.get_presence())