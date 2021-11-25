from flask import render_template, request
from app import app
from models.event_list import events, add_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Event Planner', events=events)

@app.route('/events', methods=['POST'])
def add_new_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guests = int(request.form['guests'])
    event_room = request.form['room']
    event_description = request.form['description']

    new_event = Event(event_date, event_name, event_guests, event_room, event_description)
    add_event(new_event)
    return index()