# Marshall Pigford
# Section 012
# pigford@email.sc.edu
# Jump Game

######################Logs######################

# 11/13/2024
#  - Created the Turtle for the Player
#  - Created the Turtle for the Platforms
#  - Made Code for Simple Movement

# 11/19/2024
#  - Created a function to draw a rectangle
#  - Made the Rectangles move instead of player
#    to create infinite scroll effect
#  - Made the platform react to player contact

# 11/20/2024
#  - Created the First Successful Jump
#  - For Some Reason length_of_jump Actually is
#    height_of_jump (fix that)

# 12/03/2024
#  - Created the Game, but it Needs Graphics
#  - Fixed the length_of_jump Bug
#  - Created the Infinite Scrolling Effect
#  - Made the Player Follow the Mouse Cursor

# 12/04/2024
#  - Added Graphics
#  - Added a Score
#  - Added the Ability to Lose
#  - Added Progressive Difficulty
#  - Adjusted Collision
#  - Refactored Code

####################Logs End####################

# Imports
import turtle
import time
import random

# Create Player Variables
player_x = 0
player_y = 0
player_speed = 5
player_cursor_distance = 0
player_direction = [0, -1]

# Create the Writer Turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()
writer.goto(-225, -225)

# Create the Game Window
Window = turtle.Screen()
Window.title("Parachute Pig")
Window.bgcolor("black")
Window.screensize(500, 500)
Window.tracer(0)
Window.register_shape("parachute_pig.gif")
Window.register_shape("platform.gif")

# Create Player Turtle
player = turtle.Turtle()
player.color("white")
player.shape("parachute_pig.gif")
player.speed(0)
player.left(90)
player.penup()

# Stopping Function
def stop():
    global running
    running = False

# Check For Pressed Keys
Window.listen()
Window.onkeypress(stop, "q")

# Variables
running = True # For Game Loop Control
is_jumping = False # To Make the Jumps Last Across Cycles
just_removed = False # To Make Sure that Deleting Platforms Only Removes One
draw_next = True # To Let the Program Know When to Make a New Platform
length_of_jump = -5 # To Keep Track of How Long the Player is has been Jumping
score = 0 # To Keep Track of the Score

# Draw the First Platform
num_platforms = 10
platform_coords = [[-25, -20]]
platform_direction = 1
platforms = []

# Create More Platforms
for i in range(num_platforms - 1):
    platform_coords.append([random.randint(-250, 200), random.randint(-250, 200)])

# Create Turtles to Correspond With the Platforms
for i in range(num_platforms):
    new_platform = turtle.Turtle()
    new_platform.penup()
    new_platform.hideturtle()
    new_platform.shape("platform.gif")
    new_platform.setposition(platform_coords[i][0], platform_coords[i][1])
    new_platform.showturtle()
    platforms.append(new_platform)

while running:
    # Creating a Time Buffer
    time.sleep(0.02)

    # Drawing the Platforms
    for i in range(len(platform_coords)):
        # Move the Platforms
        platforms[i].setposition(platform_coords[i][0], platform_coords[i][1])

        # If the Platform is Low Enough, Delete it
        if platform_coords[i][1] < -250:
            platform_coords.pop(i)
            platforms[i].hideturtle()
            platforms.pop(i)

            # Tell the Program to Draw Another Platform
            draw_next = True
            score += 1
            break

    # If a Platform Was Deleted, Make a New Platform
    if draw_next:
        platform_coords.append([random.randint(-250, 200), random.randint(270, 280)])
        new_platform = turtle.Turtle()
        new_platform.penup()
        new_platform.hideturtle()
        new_platform.shape("platform.gif")
        new_platform.setposition(platform_coords[-1][0], platform_coords[-1][1])
        new_platform.showturtle()
        platforms.append(new_platform)
        draw_next = False

    y_coords = []
    for i in range(len(platform_coords)):
        # Change the y-coordinate Based on Platform Direction
        platform_coords[i][1] += platform_direction * 2.5
        y_coords.append(platform_coords[i][1])
        
    for i in range(len(platform_coords)):
        # Collision Detection for Each of the Platforms
        if player.xcor() + 60 > platform_coords[i][0] + 5 and player.xcor() < 5 + platform_coords[i][0] + 50 and player.ycor() - 75 < platform_coords[i][1] and player.ycor() - 75 > platform_coords[i][1] - 10 and platform_direction > 0:
            # If Collided Correctly, Start the Jumping Sequence
            is_jumping = True
            length_of_jump = 20

    # Checks if Still Jumping
    if length_of_jump > 0.5:
        # If so, Change Direction by the Derivative of the Parabola Function
        platform_direction = -3 / 4 * (length_of_jump + 1) + 3.5
        length_of_jump -= 1
    else:
        # If not, Unflag is_jumping
        is_jumping = False

    # Draw One Less Platform After Every 100 Points
    if score % 100 == 0 and score > 0 and just_removed == False:
        num_platforms -= 1
        platforms[-1].hideturtle()
        platforms.pop(-1)
        platform_coords.pop(-1)
        just_removed = True

    # If a Platform Was Just Removed and the Score Hasn't Changed, Don't Remove Again
    if just_removed and score % 100 != 0:
        just_removed = False

    # Code to Grab the Cursor Position Without Dragging
    # For canvas = turtle.getcanvas() I retrieved it from stackoverflow
    # I added it to get the pointer position without clicking the mouse
    # turtle.getcanvas() returns an object with a method for accessing the pointer's x coordinate
    canvas = turtle.getcanvas()

    # Modified Player Cursor Distance to Move Player to Cursor by the Distance
    # canvas.winfo_pointerx() returns the x coordinate of the mouse cursor
    # I subtract the player position from the mouse position to get the distance the player should move
    # The use of turtle.getcanvas() and canvas.winfo_pointerx() has been approved by Professor Delahunt
    player_cursor_distance = ((canvas.winfo_pointerx() - player.xcor() - 750) / 10)
    player.setx(player.xcor() + player_cursor_distance)

    # Draw the Score on the Screen
    writer.clear()
    writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    # Check if the Player Can no Longer hit a Platform; If so, Game Over
    if min(y_coords) > player.ycor() + 200:
        writer.clear()
        writer.goto(0, -50)
        writer.write(f"Game Over! \nFinal Score: {score}", align="center", font=("Arial", 24, "normal"))
        running = False   
    Window.update()

time.sleep(1)
turtle.bye()
