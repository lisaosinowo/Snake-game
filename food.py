from turtle import Turtle
import random

class Food(Turtle): # We want to inherit the Turtle object in the Food class
    # Turtle is the superclass (the class we're inheriting from)
    # We can now use things from the Turtle class in the new Food class

    def __init__(self):
        super().__init__() # super().__init__() is needed when we use a superclass
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

        # We're only able to use these Turtle methods as we're inheriting from the Turtle class.
        # If we don't inherit the Turtle class on line 3 then we can't use the methods on lines 9 - 11
     
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

