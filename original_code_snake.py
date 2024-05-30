from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # bitno je da ovaj atribut ide ispod pozivanja metode create_snake(), jer se tek tom metodom kreiraju segmenti i dodaju u listu segments
        # kada bi taj atribut napisali ispred pozivanja metode create_snake, dobili bismo grešku jer u tom trenutku je lista segments zapravo prazna
        self.head = self.segments[0]

    def create_snake(self):
        x_position = 0
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=x_position, y=0)
            x_position -= 20
            self.segments.append(new_segment)

    def grow_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        x_cor_last_segment = self.segments[-1].xcor
        y_cor_last_segment = self.segments[-1].ycor
        new_segment.goto(x=x_cor_last_segment, y=y_cor_last_segment)
        self.segments.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # ako se prvi segment kreće prema dolje, tada se ne moe okrenuti prema gore (zmija ne može ići sama u sebe)
        # metoda heading() će izbaciti smjer kretanja segmenta u obliku nagiba u stupnjevima (npr. 0, 90...)
        if self.head.heading() != DOWN:
            # želimo promjijeniti smjer prvog segmenta, jer ostali segmenti će slijediti njegovu putanju
            # self.segments[0].setheading(UP) - dobili bismo isto, no sada smo u init kreirali atribut self.head
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
