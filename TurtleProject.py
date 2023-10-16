from turtle import Turtle, Screen

kev = Turtle()
kev.shape("turtle")
kev.color("red")
for _ in range(4):
    kev.forward(-100)
    kev.circle(-100)
    kev.fd(100)
    kev.right(90)
    kev.circle(100)
    kev.backward(10)


    def draw_spirogragh(size_of_gap):
        for _ in range(int(960 / size_of_gap)):
            kev.speed(11)
            kev.circle(100)
        kev.setheading(kev.heading() + size_of_gap)

    draw_spirogragh(12)






screen = Screen()
screen.exitonclick()
