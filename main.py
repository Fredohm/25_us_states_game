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


correct_answers = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    for state in df.state:
        if state.lower() == answer_state.lower():
            correct_answers += 1
            state_row = df[df.state == state]
            write_state(answer_state, int(state_row.x), int(state_row.y))
            print(f"x: {state_row.x}, y: {state_row.y}")
turtle.mainloop()
