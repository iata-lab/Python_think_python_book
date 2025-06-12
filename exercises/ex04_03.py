import turtle

# 1
def cuadrado(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

bob = turtle.Turtle()
cuadrado(bob)
turtle.done()


# 2
def cuadrado(t, longitud):
    for i in range(4):
        t.forward(longitud)
        t.left(90)

bob = turtle.Turtle()
cuadrado(bob, 150)  
turtle.done()

# 3
def poligono(t, longitud, n):
    for i in range(n):
        t.forward(longitud)
        t.left(360 / n)

bob = turtle.Turtle()
poligono(bob, 100, 6)  
turtle.done()