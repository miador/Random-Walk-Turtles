import random
import turtle
import math

colors = ["red", "blue", "green", "orange"]

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def print_score(undo):
    score_str = ""
    for player in players:
        score_str = score_str + "{}:{}  "\
                     .format(player["name"], player["score"])
    if undo:
        score_turtle.undo()
    score_turtle.write(score_str, align="center",
                       font=("Arial", 14, "normal"))


wn = turtle.Screen()

leftBound = -(wn.window_width() / 2)
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -(wn.window_height() / 2)

awards = []
while len(awards) < 5:
    x = random.randrange(leftBound+20, rightBound-20)
    y = random.randrange(bottomBound+20, topBound-20)
    too_close = False
    for award in awards:
        if distance(x,y,award[0],award[1]) < 30:
            too_close = True
    if not too_close:
        awards.append([x,y])

print(awards)

drawer_turtle = turtle.Turtle()
drawer_turtle.shape("circle")
drawer_turtle.penup()
drawer_turtle.fillcolor("pink")
drawer_turtle.hideturtle()

n = 1
for award in awards:
    drawer_turtle.goto(award[0],award[1])
    drawer_turtle.stamp()
    # drawer_turtle.write(n)
    n = n + 1

drawer_turtle.color("white", "white")

def isInScreen(w, t):

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


def move_player(player_dict):
    a_turtle = player_dict["turtle"]
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        a_turtle.left(random.randrange(30, 45))
    else:                      # tails
        a_turtle.right(random.randrange(30, 45))
    a_turtle.forward(10)
    award_eaten = None
    for award in awards:
        if distance(a_turtle.xcor(),a_turtle.ycor(),award[0],award[1]) < 10:
            award_eaten = award
    if award_eaten != None:
        player_dict["score"] += 10
        awards.remove(award_eaten)
        drawer_turtle.goto(award_eaten[0], award_eaten[1])
        drawer_turtle.stamp()
        print_score(True)

    if not isInScreen(wn, a_turtle):
        a_turtle.left(180)
        a_turtle.forward(10)
    
def create_walker_turtle(turtle_color):
   new_turtle = turtle.Turtle()
   new_turtle.shape('turtle')
   new_turtle.speed(9) 
   new_turtle.color(turtle_color, turtle_color)
   new_turtle.pensize(5)
   new_turtle.penup()
   return new_turtle


players = []

for color in colors:
    player = {}
    name = input("Enter player name: ")
    player["turtle"] = create_walker_turtle(color)
    player["color"] = color
    player["score"] = 0
    player["name"] = name
    players.append(player)


score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0,topBound - 30)
print_score(False)

while len(awards)>0:
    for player in players:
        move_player(player)

print("STOPPED")
wn.exitonclick()



