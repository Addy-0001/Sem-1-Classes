import turtle

b = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.color("black", "red")

t.penup()
t.goto(-100, 100)
t.pendown()
t.circle(10)

t.penup()
t.goto(100, 100)
t.pendown()
t.circle(10)

t.penup()
t.goto(0, 0)
t.pendown()
t.circle(10)


t.penup()
t.goto(-100, -100)
t.pendown()
t.circle(10)

t.penup()
t.goto(100, -100)
t.pendown()
t.circle(10)

t.ht()

turtle.mainloop()
