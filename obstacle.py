from turtle import Turtle

class Obstacle:
    def __init__(self, position, pattern, repeat_times, piece_size):
        self.pieces = []
        self.create_obstacle(position, pattern, repeat_times, piece_size)

    def create_obstacle(self, position, pattern, repeat_times, piece_size):
        start_x, start_y = position
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])

        for repeat in range(repeat_times):
            for i in range(pattern_rows):
                for j in range(pattern_cols):
                    if pattern[i][j] == 1:
                        piece = Turtle("square")
                        piece.color("#3DFF45")
                        piece.shapesize(stretch_wid=piece_size / 20,
                                        stretch_len=piece_size / 20)
                        piece.penup()
                        piece.goto(start_x + j * piece_size + repeat * pattern_cols * piece_size,
                                   start_y - i * piece_size)
                        self.pieces.append(piece)

    def check_collision(self, projectile):
        for piece in self.pieces:
            if piece.distance(projectile) < 15:  # Adjust collision distance as necessary
                piece.hideturtle()
                self.pieces.remove(piece)
                return True
        return False

