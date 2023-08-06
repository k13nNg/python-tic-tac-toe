from turtle import *

screen = Screen()
# Set game window size
screen.setup(800, 800)
# Set title of the window
screen.title("Tic_Tac_Toe")
# Get rid of the tracing, get the image in instant time
screen.tracer(0,0) 
t = Turtle()
t.hideturtle()

player_turn = 0
game_over = False

# Provided constants

# Coordinates for drawing the board and checking the mouse click
HORIZONTAL_LEFT = -225
HORIZONTAL_RIGHT = 225
HORIZONTAL_TOP = 75
HORIZONTAL_BOTTOM = -75
VERTICAL_LEFT = -75
VERTICAL_RIGHT = 75
VERTICAL_TOP = 225
VERTICAL_BOTTOM = -225
OFF_SET_FACTOR = 30

# Flag variables to check for already clicked grid
TOP_LEFT = -1
TOP_MIDDLE = -1
TOP_RIGHT = -1

MID_LEFT = -1
MID_MIDDLE = -1
MID_RIGHT = -1

BOTTOM_LEFT = -1
BOTTOM_MIDDLE = -1
BOTTOM_RIGHT = -1

# draw_board() draws the board
def draw_board():
    # draw horizontal lines
    t.width(10)
    t.penup()
    t.setpos(HORIZONTAL_LEFT, HORIZONTAL_TOP)
    t.pendown()
    t.goto(HORIZONTAL_RIGHT,HORIZONTAL_TOP)
    t.penup()

    t.setpos(HORIZONTAL_LEFT, HORIZONTAL_BOTTOM)
    t.pendown()
    t.goto(HORIZONTAL_RIGHT,HORIZONTAL_BOTTOM)
    t.penup()

    # draw vertical lines
    t.setpos(VERTICAL_LEFT, VERTICAL_TOP)
    t.pendown()
    t.goto(VERTICAL_LEFT, VERTICAL_BOTTOM)
    t.penup()
    
    t.setpos(VERTICAL_RIGHT, VERTICAL_TOP)
    t.pendown()
    t.goto(VERTICAL_RIGHT, VERTICAL_BOTTOM)
    t.penup()

# draw player (x_1, y_1, x_2, y_2, player) draws the symbol for the player at the given grid positioned by (x_1, y_1, x_2, y_2)
def draw_player(x_1, y_1, x_2, y_2, player):
    if (player % 2 == 0):
        t.pencolor('blue')
        t.setpos(x_1 + OFF_SET_FACTOR, y_1 - OFF_SET_FACTOR)
        t.pendown()
        t.goto(x_2 - OFF_SET_FACTOR, y_2 + OFF_SET_FACTOR)
        t.penup()
        t.setpos(x_2 - OFF_SET_FACTOR, y_1 - OFF_SET_FACTOR)
        t.pendown()
        t.goto(x_1 + OFF_SET_FACTOR, y_2 + OFF_SET_FACTOR)
        t.penup()
    else:
        t.pencolor('red')
        t.goto((x_1 + x_2) // 2, y_2 + OFF_SET_FACTOR)
        t.pendown()
        t.circle(50)
        t.penup()

    screen.update()

# get_player(player_turn) returns 'X' or 'O' depends on the value of player_turn
def get_player(player_turn):
    if (player_turn % 2 == 0):
        return 'X'
    else:
        return 'O'

# horizontal_check_and_draw(x, y, x_2, y_2) draws the approriate symbol of the player on the grid according to 
# the position of the mouse click
def horizontal_check_and_draw(x, y, x_2, y_2):
    global TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, MID_LEFT, MID_MIDDLE, MID_RIGHT, BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT, player_turn

    if (HORIZONTAL_LEFT < x and x < VERTICAL_LEFT):
        if ((y_2 == HORIZONTAL_TOP and TOP_LEFT != -1) or
            (y_2 == HORIZONTAL_BOTTOM and MID_LEFT != -1) or
            (y_2 == VERTICAL_BOTTOM and BOTTOM_LEFT != -1)):
            return
        else:
            if (y_2 == HORIZONTAL_TOP):
                TOP_LEFT = get_player(player_turn)

            elif (y_2 == HORIZONTAL_BOTTOM):
                MID_LEFT = get_player(player_turn)
            else:
                BOTTOM_LEFT = get_player(player_turn)
            
            draw_player(HORIZONTAL_LEFT, x_2, VERTICAL_LEFT, y_2, player_turn)

    elif(VERTICAL_LEFT < x and x < VERTICAL_RIGHT):
        if ((y_2 == HORIZONTAL_TOP and TOP_MIDDLE != -1) or
            (y_2 == HORIZONTAL_BOTTOM and MID_MIDDLE != -1) or
            (y_2 == VERTICAL_BOTTOM and BOTTOM_MIDDLE != -1)):
            return
        else:
            if (y_2 == HORIZONTAL_TOP):
                TOP_MIDDLE = get_player(player_turn)

            elif (y_2 == HORIZONTAL_BOTTOM):
                MID_MIDDLE = get_player(player_turn)
            else:
                BOTTOM_MIDDLE = get_player(player_turn)

        draw_player(VERTICAL_LEFT, x_2, VERTICAL_RIGHT, y_2, player_turn)


    elif(VERTICAL_RIGHT < x and x < HORIZONTAL_RIGHT):
        if ((y_2 == HORIZONTAL_TOP and TOP_RIGHT != -1) or
            (y_2 == HORIZONTAL_BOTTOM and MID_RIGHT != -1) or
            (y_2 == VERTICAL_BOTTOM and BOTTOM_RIGHT != -1)):
            return
        
        else:
            if (y_2 == HORIZONTAL_TOP):
                TOP_RIGHT = get_player(player_turn)
            elif (y_2 == HORIZONTAL_BOTTOM):
                MID_RIGHT = get_player(player_turn)
            else:
                BOTTOM_RIGHT = get_player(player_turn)

        draw_player(VERTICAL_RIGHT, x_2, HORIZONTAL_RIGHT, y_2, player_turn)

    player_turn += 1


# check_diagonal() will return the symbol of the winning player if they have 3 same symbols in a diagonal, return -1 if we don't have a winner
def check_diagonal():
    if (TOP_LEFT == MID_MIDDLE and MID_MIDDLE == BOTTOM_RIGHT):
        return TOP_LEFT
    
    elif(TOP_RIGHT == MID_MIDDLE and MID_MIDDLE == BOTTOM_LEFT):
        return TOP_RIGHT

    else:
        return -1

# check_vertical() will return the symbol of the winning player if they have 3 same symbols in a vertical line, return -1 if we don't have a winner
def check_vertical():
    if (TOP_LEFT == MID_LEFT and MID_LEFT == BOTTOM_LEFT):
        return TOP_LEFT
    elif (TOP_MIDDLE == MID_MIDDLE and MID_MIDDLE == BOTTOM_MIDDLE):
        return TOP_MIDDLE
    elif (TOP_RIGHT == MID_RIGHT and MID_RIGHT == BOTTOM_RIGHT):
        return TOP_RIGHT
    else:
        return -1

# check_horizontal() will return the symbol of the winning player if they have 3 same symbols in a horizontal line, return -1 if we don't have a winner
def check_horizontal():
    if (TOP_LEFT == TOP_MIDDLE and TOP_MIDDLE == TOP_RIGHT):
        return TOP_LEFT
    elif (MID_LEFT == MID_MIDDLE and MID_MIDDLE == MID_RIGHT):
        return MID_LEFT
    elif (BOTTOM_LEFT == BOTTOM_MIDDLE and BOTTOM_MIDDLE == BOTTOM_RIGHT):
        return BOTTOM_LEFT
    else:
        return -1

# check_winner() returns the symbol of the winner, return -1 if there is no winner yet
def check_winner():

    if (check_diagonal() != -1):
        return check_diagonal()
    elif (check_vertical() != -1):
        return check_vertical()
    elif (check_horizontal() != -1):
        return check_horizontal()
    else:
        return -1
    
# get_mouste_click_coor(x, y) collect the position of the mouse click and display the approriate symbol according to the player's turn
def get_mouse_click_coor(x, y):
    global game_over

    if (game_over == False):
        if (HORIZONTAL_TOP < y and y < VERTICAL_TOP):
            horizontal_check_and_draw(x, y, VERTICAL_TOP, HORIZONTAL_TOP)        
            

        elif (HORIZONTAL_BOTTOM < y and y < HORIZONTAL_TOP):

            horizontal_check_and_draw(x, y, HORIZONTAL_TOP, HORIZONTAL_BOTTOM)

        elif (VERTICAL_BOTTOM < y and y < HORIZONTAL_BOTTOM):

            horizontal_check_and_draw(x, y, HORIZONTAL_BOTTOM, VERTICAL_BOTTOM)
    
    if (check_winner() != -1):
        game_over = True
        t.clear()
        t.goto(0, 0)
        t.write("Player %s won!" % check_winner(), font=("Verdana", 50, "normal"), align="center")

# start the game by draw an empty board
draw_board()

# capture the mouse click of the user
screen.onclick(get_mouse_click_coor)

# tells turtle to compile and display the above code
mainloop()