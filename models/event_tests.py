import unittest
from models.event import Event
from models.event_list import events, add_event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event = Event("25/11/2021", "Graduation", 15, "Winter room", "PSD graduation")

    def test_has_date(self):
        expected = "25/11/2021"
        actual = self.event.date
        self.assertEqual(expected, actual)

    def test_has_name(self):
        expected = "Graduation"
        actual = self.event.name
        self.assertEqual(expected, actual)

    def test_has_num_guests(self):
        expected = 15
        actual = self.event.guests
        self.assertEqual(expected, actual)

    def test_has_room(self):
        expected = "Winter room"
        actual = self.event.room
        self.assertEqual(expected, actual)

    def test_has_description(self):
        expected = "PSD graduation"
        actual = self.event.description
        self.assertEqual(expected, actual)

    def test_add_event(self):
        add_event(self.event)
        expected = 1
        actual = len(events)
        self.assertEqual(expected, actual)
