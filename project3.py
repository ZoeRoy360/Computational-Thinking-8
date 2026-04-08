from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 160
x2 = -250
y2 = 70
x3 = -250
y3 = -20
x4 = -250
y4 = -105


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("racetrack")
t1 = create_sprite("dog1",x1,y1)
t2 = create_sprite("dog2",x2,y2)
t3 = create_sprite("dog3",x3,y3)
t4 = create_sprite("dog4",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    x1 += random.randint(50,100)
    x2 += random.randint(50,100)
    x3 += random.randint(50,100)
    x4 += random.randint(50,100)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
elif
    s5.write("player 2 wins!")


turtle.exitonclick()