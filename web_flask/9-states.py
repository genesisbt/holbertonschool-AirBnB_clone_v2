#!/usr/bin/python3
""" Flask Application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def display_states(state_id=None):
    """
    Display states based on the provided ID.
    """
    states_list = []
    all_states = storage.all(State)
    if state_id is None:
        for key in all_states:
            states_list.append(all_states[key])
    else:
        state_key = 'State.' + state_id
        states_list = all_states.get(state_key)
    return render_template('9-states.html', states=states_list, id=state_id)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Close SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)