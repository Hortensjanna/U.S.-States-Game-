import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_states = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?")

    current_state = data[data.state == answer_state]
    state_name = current_state.state
    x_cor = int(current_state.x)
    y_cor = int(current_state.y)
    correct_states += 1

    writing = turtle.Turtle()
    writing.penup()
    writing.hideturtle()
    writing.goto(x_cor, y_cor)
    writing.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))



screen.exitonclick()