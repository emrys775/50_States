
import turtle
import math
import pandas
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
available_states = []
state_turtles = {}

for state in all_states:n
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(300, 250 - all_states.index(state) * 20)  # Position on the right
    t.write(state)
    t.showturtle()
    state_turtles[state] = t
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for draggable_state, draggable_turtle in state_turtles.items():
        draggable_turtle.ondrag(lambda x, y, state=draggable_state: handle_drag(x, y, state))
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.speed(0)

        t.write(answer_state)

def handle_drag(x, y, state):
    draggable_turtle = state_turtles[state]
    draggable_turtle.goto(x, y)
    state_data = data[data.state == state]
    correct_x, correct_y = state_data.x.item(), state_data.y.item()
    distance = math.sqrt((correct_x - x) ** 2 + (correct_y - y) ** 2)
    if distance < 20:
        draggable_turtle.color("green")
    else:
        draggable_turtle.color("red")


