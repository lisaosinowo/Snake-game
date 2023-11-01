from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# Anything you need to create the class needs to be above the class initiation
# e.g if you need to use Turtle when making a class it needs to be above

class Snake():

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position)
            snake_part.pencolor("black")
            self.snake_parts.append(snake_part)

    def move(self):
         for snake_num in range(len(self.snake_parts) - 1, 0, -1): # The range starts at the length of the snake parts
            # The range ends at 0, and the -1 is used to count down to 0.
            new_x_coord = self.snake_parts[snake_num - 1].xcor() 
            new_y_coord = self.snake_parts[snake_num - 1].ycor()
            # Lines 31 & 32 obtain the x and y coordinates of the second to last snake part
            self.snake_parts[snake_num].goto(new_x_coord, new_y_coord) 
            # Line 34 makes sure that each snake part moves to the position before it.
            # E.g the last snake part 3 will move to where the coordinate for the 2nd snake part was before to make the parts move.    
         self.head.forward(MOVE_DISTANCE) # This moves the very first snake part fowards which leads the snake (moving the snake head)
         # Line 28 to 37 moves the snake parts (moves the entire snake)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # Since in the game the snake is not allowed to go back on itself, we need to implement that
            # The snake can't go in the opposite direction
            # If the snake is going in the upward direction it can't go downwards immediately
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Once the head of the snake turns one way the rest of the body will follow the direction of the head
        
    def add_to_tail(self):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.pencolor("black")
        self.snake_parts.append(snake_part)

    def hit_tail(self):
        if self.head.distance(self.snake_parts[-1]) < 15:
            return True
        else:
            return False
