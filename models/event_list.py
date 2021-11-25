from models.event import Event

event_1 = Event("25/11/2021", "Graduation", 15, "Winter room", "PSD graduation")
event_2 = Event("30/11/2021", "Birthday party", 25, "Upper room", "Guilherme's 39th")

events = [event_1, event_2]

def add_event(event):
    events.append(event)