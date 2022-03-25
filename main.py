from turtle import Screen
import pandas
from state_label import State_Label

screen = Screen()
screen.bgpic("./blank_states_img.gif")
screen.title("US States Game")
screen.setup(725, 491)

state_data = pandas.read_csv("./50_states.csv")
states = state_data.state.to_list()

counter = 0
while counter < 50:
    user_guess = screen.textinput("Guess a state", f"Enter a state name ({counter}/50).").title()
    if user_guess in states:
        # Get row
        found_state = state_data[state_data.state == user_guess]

        # Remove user_guess from states
        states.remove(user_guess)

        # Get plotting details
        state_name = found_state.state.item()
        x = int(found_state.x)-5
        y = int(found_state.y)-5

        # Plot state
        t = State_Label(state_name, x, y)

        # Increase counter
        counter += 1

screen.mainloop()
