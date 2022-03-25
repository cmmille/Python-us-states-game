from turtle import Turtle
class State_Label(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(x, y)
        self.write(state_name)