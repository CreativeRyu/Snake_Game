from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_speed = 0.2

    # Creates the Segment Objects of the snake
    # and saves them into a list of segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("SlateGray")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # def growing_up(self):
    #     tail_index = len(self.segments)-1
    #     current_tail = self.segments[tail_index]
    #     tail_position = current_tail.xcor(), current_tail.ycor()
    #     self.add_segment(tail_position)

    def grow_up(self):
        self.add_segment(self.segments[-1].position())
        self.move_speed *= 0.95

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("SlateGray")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Zusammenhängende Fortbewegung der Segmente
# Holt die Koordinaten des vorherigen Segments und
# bewegt das aktuelle Segment auf diese Koordinaten
    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(MOVEMENT_SPEED)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
