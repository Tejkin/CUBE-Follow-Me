from event import Event
from location_events import LocationEvents

if __name__ == '__main__':

    kitchen = Event("kitchen",)
    bedroom = Event("bedroom")
    living_room = Event("living room")
    
    moved = LocationEvents()

    kitchen.set_motion(False)
    kitchen.set_motion(True)

    for events in allEvents:
        if events.check_presence_change() == True:
            moved.add_event(events.get_location())
            break
        else:
            break

    while True:
        if kitchen.check_presence_change() == True:
            moved.add_event(kitchen.get_location())
            break
        else:
            break
    print(moved.all_motion)
