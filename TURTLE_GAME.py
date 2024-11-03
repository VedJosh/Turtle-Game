import turtle, random
import time

screen = turtle.Screen()
screen.setup(width=500,height=400)

turtles_dictionary = {}

# drawing the finish line
def draw_finishline():
    # screen.bgcolor()
    finishline = turtle.Turtle()
    finishline.up()
    finishline.shapesize(4)
    finishline.goto(250,150)
    finishline.setheading(-90)
    finishline.down()
    finishline.pensize(6)
    finishline.color('black')
    finishline.write('FINISH LINE',align='center',font=20)
    finishline.forward(400)

def initialize_turtles():
    y_position = -150
    color_list = ['red','yellow','green','pink','blue','orange']
    color_index = 0
    for i in range(6):
        player = turtle.Turtle()
        player.shape('turtle')
        player.shapesize(2)

        color_of_turtle = color_list[color_index]
        player.color(color_of_turtle)
        # setting up the turtle to their position
        player.up()
        player.setposition(-250,y_position)

        color_index+=1
        y_position+=50
        # adding each turtle to the dictionary
        turtles_dictionary[color_of_turtle]=player

def game():
    global is_play
    draw_finishline()
    initialize_turtles()
    user_guess = screen.textinput('CAN YOU GUESS?','Guess the color of the turtle:').lower()
    isgame_over = False
    while not isgame_over:
        for each_player in turtles_dictionary:
            (turtles_dictionary[each_player]).forward(random.randint(1,20))
            if (turtles_dictionary[each_player]).pos()[0]>250:
                isgame_over=True
                winner = each_player
    if user_guess==winner:
        is_play = screen.textinput('You WIN','Wanna Play once more? (yes/no)').lower()
    else:
        is_play = screen.textinput('You LOSE','Wanna Play once more? (yes/no)').lower()
    screen.clear()
is_play = 'yes'
while is_play=='yes':
    game()
else:
    screen.bgcolor('green')
    exit1 = turtle.Turtle()
    exit1.write('GAME OVER',align='center', font=50)
    exit1.color('white')
    time.sleep(3)
    screen.bye()
