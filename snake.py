from turtle import Turtle, Screen


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_assegment(position)
    
    
    def add_assegment(self, position):
            newsegment = Turtle("square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(position)
            self.segments.append(newsegment)
    
    def extend(self):
        self.add_assegment(self.segments[-1].position())
        

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:  
            self.segments[0].setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)