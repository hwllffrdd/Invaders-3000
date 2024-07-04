from invader import SpaceInvader
from projectile import Projectile
import random

class Fleet:
    def __init__(self, rows, cols, start_position, shape_image, h_space, v_space):
        self.invaders = []
        self.create_fleet(rows, cols, start_position, shape_image, h_space, v_space)
        self.direction = 1
        self.speed = 10
        self.descend_distance = 10
        self.move_speed = 250

    def create_fleet(self, rows, cols, start_position, shape_image, h_space, v_space):
        start_x, start_y = start_position
        for i in range(rows):
            for j in range(cols):
                invader = SpaceInvader((start_x + j * h_space, start_y - i * v_space), shape_image)
                self.invaders.append(invader)

    def move(self):
        global game_over
        for invader in self.invaders:
            if invader.is_alive:
                invader.move(self.speed * self.direction, 0)

        # Check if any invader has hit the screen boundary and descend
        if any(invader.xcor() > 280 or invader.xcor() < -280 for invader in self.invaders if invader.is_alive):
            self.direction *= -1
            for invader in self.invaders:
                if invader.is_alive:
                    invader.move(0, -self.descend_distance)
                    # Check if the invaders reached the bottom of the screen
                    if invader.ycor() < -150:
                        game_over = True
                        return "game_over"

    def shoot(self):
        living_invaders = [invader for invader in self.invaders if invader.is_alive]
        if living_invaders:
            shooter_invader = random.choice(living_invaders)
            return Projectile(shooter_invader.position(), "invader")

    def adjust_speed(self):
        self.move_speed *= 0.99  # Adjust the speed

    def check_collision(self, projectile):
        for invader in self.invaders:
            if invader.is_alive and invader.distance(projectile) < 15:  # Adjust collision distance as necessary
                invader.destroy()
                return True
        return False
