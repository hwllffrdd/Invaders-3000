import turtle
from shooter import Shooter
from obstacle import Obstacle
from fleet import Fleet
from display import Display, display_message
import random

screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("")
screen.tracer(0)

screen.addshape("shooter.gif")
screen.addshape("invader.gif")

shooter_projectiles = []
invader_projectiles = []

game_over = False

def handle_shoot(projectile):
    shooter_projectiles.append(projectile)

def invader_shoot():
    projectile = fleet.shoot()
    if projectile:
        invader_projectiles.append(projectile)
    screen.ontimer(invader_shoot, random.randint(500, 2500))

display = Display(position=(-290, -390))

shooter = Shooter((0, -350), handle_shoot, display)

pattern = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
]

obstacle = Obstacle((-270, -150), pattern=pattern, repeat_times=5, piece_size=7)

fleet = Fleet(rows=3, cols=10, start_position=(-200, 350), shape_image="invader.gif", h_space=40, v_space=40)


# Function to move all projectiles and check for collisions
def move_projectiles():
    global shooter_projectiles, invader_projectiles, game_over

    if game_over:
        return

    # Move shooter's projectiles
    for projectile in shooter_projectiles:
        projectile.move()
        # Check for collision with target or invaders
        if projectile.check_collision(obstacle) or fleet.check_collision(projectile):
            projectile.hideturtle()
            shooter_projectiles.remove(projectile)
        # Remove the projectile if it goes off-screen
        elif projectile.ycor() > 400:
            projectile.hideturtle()
            shooter_projectiles.remove(projectile)

    # Move invader's projectiles
    for projectile in invader_projectiles:
        projectile.move()
        # Check for collision with target or shooter
        if projectile.check_collision(obstacle) or projectile.distance(shooter) < 15:
            if projectile.distance(shooter) < 15:
                # Handle shooter collision
                shooter.lose_life()
                if shooter.lives == 0:
                    game_over = True
                    return  # Stop the game loop if the game is over
            projectile.hideturtle()
            invader_projectiles.remove(projectile)
        # Remove the projectile if it goes off-screen
        elif projectile.ycor() < -400:
            projectile.hideturtle()
            invader_projectiles.remove(projectile)

    # Check for collisions between shooter's and invader's projectiles
    for s_projectile in shooter_projectiles:
        for i_projectile in invader_projectiles:
            if s_projectile.distance(i_projectile) < 5:
                s_projectile.hideturtle()
                i_projectile.hideturtle()
                shooter_projectiles.remove(s_projectile)
                invader_projectiles.remove(i_projectile)
                break



def update_fleet():
    global game_over
    result = fleet.move()
    if result == "game_over":
        display_message("GAME OVER")
        game_over = True
        return
    screen.update()
    fleet.adjust_speed()
    if all(not invader.is_alive for invader in fleet.invaders):
        display_message("YOU WIN!")
        game_over = True
        return
    screen.ontimer(update_fleet, int(fleet.move_speed))



screen.listen()
screen.onkey(shooter.go_left, "Left")
screen.onkey(shooter.go_right, "Right")
screen.onkey(shooter.shoot, "space")

update_fleet()
invader_shoot()

def game_loop():
    global game_over
    if not game_over:
        move_projectiles()
        screen.update()
        screen.ontimer(game_loop, 16)  # About 60 FPS

game_loop()

screen.exitonclick()
