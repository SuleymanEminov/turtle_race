from turtle import Turtle as t, Screen
import random

# create screen and give size
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500,height=400)

colors = ['green','red','yellow','purple','orange'] # colors of turtles
y_positions = [160,80,0,-80,-160]                   # y positions of turtles
all_turtles = []                                    # keep turtles in list

# create turtles
def main():
    flag = True
    create_turtle()     # create turtles
    while flag:
        user_bet = screen.textinput("Make a bet", "Who is gonna win?") # make your bet
        winner = start_race(user_bet) # get winner

        # print race results and ask for replay
        print(f"Winner is: {winner}")
        if winner == user_bet:
            print("YOU WON!")
            answer = screen.textinput("WINNER", 'You won. Type "yes" to play again or type "no" to exit.')
            flag = replay(answer)

        else:
            print("You lost")
            answer = screen.textinput("LOST", 'you lost. Type "yes" to play again or type "no" to exit.')
            flag = replay(answer)

def create_turtle():
    for turtle_index in range(0,5): # create 5 turtles and set their positions
        new_turtle = t("turtle")    # make pens turtles
        new_turtle.color(colors[turtle_index])      # give color
        new_turtle.penup()                          # penup
        new_turtle.goto(x=-220,y=y_positions[turtle_index]) # set position
        all_turtles.append(new_turtle)                      # add turtle to all_turtles



def start_race(bet):
    is_race_on = False      # race flag
    if bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:           # 230 is finish line
                winning_turtle = turtle.pencolor()  # get color of the winner
                is_race_on = False  # end race
            else:
                random_distance = random.randint(0,10)  # move turtles in random speed
                turtle.forward(random_distance)

    return winning_turtle

def replay(user_answer):
    again = True
    if user_answer == "yes":
        again = True
        restart() # call restart to set turtles in the start line
    else:
        again = False

    return again

def restart():
    for i, turtle_index in enumerate(all_turtles):
        turtle_index.goto(x=-220, y=y_positions[i])  # set position



main()  #Call the main function

screen.exitonclick() # exit program
