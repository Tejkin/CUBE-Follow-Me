from event import Event
from location_events import LocationEvent

if __name__ == '__main__':

    kitchen = LocationEvent("kitchen",)
    bedroom = LocationEvent("bedroom")
    living_room = LocationEvent("living room")
    


    kitchen.set_motion(False)
    kitchen.set_motion(True)

    while True:
        if kitchen.check_presence_change() == True:
            kitchen.add_event(kitchen.get_location(), kitchen.get_past_presence(), kitchen.get_presence())
            break
        else:
            break
    print(kitchen.all_motion)
