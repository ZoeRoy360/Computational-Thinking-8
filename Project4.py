from utils import *

# Section 1 - setup
set_background("bedroom")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
love = 0
cats = 0
cat_list = []
# OPTIONAL: use this invisible alien to say a message


# Section 2 - controls
# TODO - define an action. ex: def my_control()
def addcat():
    global cats
    cats += 1
    x = random.randint (-300,300)
    y = random.randint (-150,150)
    c1 = create_sprite("cat1",x,y)
    cat_list.append(c1)
window.onkeypress(addcat, "space")

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control
def addlove():
    global love
    global cats
    if cats >= 5:

        love += 1
        cats -= 5
        x = random.randint (-300,300)
        y = random.randint (-150,150)
        create_sprite("heart",x,y)
        for i in range(5):
            c1 = cat_list.pop()
            c1.hideturtle()
window.onkeypress(addlove, "l")



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # m1.clear()
    # m1.write("Hello")

    time.sleep(0.01)
    window.update()
#The goal of my game is to get more cats, so that you can get more hearts, and be loved!