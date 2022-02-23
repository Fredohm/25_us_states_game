import turtle
import pandas


def write_state(p_answer, x, y):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.write(p_answer)


df = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in df.state:
            if state not in guessed_states:
                missing_states.append(state)
                missing_states_dict = {
                    "state": missing_states
                }
                states_to_learn = pandas.DataFrame(missing_states_dict)
                states_to_learn.to_csv("states_to_learn.csv")
        break

    for state in df.state:
        if state == answer_state:
            if state not in guessed_states:
                guessed_states.append(state)
                state_row = df[df.state == state]
                write_state(state_row.state.item(), int(state_row.x), int(state_row.y))
