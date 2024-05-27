import turtle
import time
import random

delay = 0.3
skor = 0
topscore = 0

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("pink")
pencere.setup(width=600, height=600)

bas = turtle.Turtle()
bas.shape("square")
bas.color("green")
bas.penup()
bas.goto(0, 0)
bas.direction = "stop"

yem = turtle.Turtle()
renkler = random.choice(["white", "yellow", "blue"])
yem.speed(0)
yem.shape('triangle')
yem.color(renkler)
yem.penup()
yem.goto(0, 100)

kuyruk = []
kalem = turtle.Turtle()
kalem.speed(0)
kalem.shape("square")
kalem.color("yellow")
kalem.hideturtle()
kalem.penup()
kalem.goto(0, 250)
kalem.write("SKOR : 0 TOP SKOR : 0", align="center", font=("candara", 20, "bold"))

def yukarigit():
    if bas.direction != "down":
        bas.direction = "up"

def asagigit():
    if bas.direction != "up":
        bas.direction = "down"

def solagit():
    if bas.direction != "right":
        bas.direction = "left"

def sagagit():
    if bas.direction != "left":
        bas.direction = "right"

def hareket():
    if bas.direction == "up":
        y = bas.ycor()
        bas.sety(y + 20)
    if bas.direction == "down":
        y = bas.ycor()
        bas.sety(y - 20)
    if bas.direction == "left":
        x = bas.xcor()
        bas.setx(x - 20)
    if bas.direction == "right":
        x = bas.xcor()
        bas.setx(x + 20)

pencere.listen()
pencere.onkeypress(yukarigit, "w")
pencere.onkeypress(asagigit, "s")
pencere.onkeypress(solagit, "a")
pencere.onkeypress(sagagit, "d")

while True:
    pencere.update()


    if bas.xcor() > 290 or bas.xcor() < -290 or bas.ycor() > 290 or bas.ycor() < -290:
        time.sleep(1)
        bas.goto(0, 0)
        bas.direction = "stop"


        if skor > topscore:
            topscore = skor

        skor = 0
        delay = 0.1


        for segment in kuyruk:
            segment.goto(1000, 1000)
        kuyruk.clear()

        kalem.clear()
        kalem.write("SKOR : {} TOP SKOR : {}".format(skor, topscore), align="center", font=("candara", 20, "bold"))


    if bas.distance(yem) < 15:
        skor += 10
        delay = delay*0.9
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        yem.goto(x, y)


        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("green")
        yeni_kuyruk.penup()
        kuyruk.append(yeni_kuyruk)


        kalem.clear()
        kalem.write("SKOR : {} TOP SKOR : {}".format(skor, topscore), align="center", font=("candara", 20, "bold"))


    for i in range(len(kuyruk) - 1, 0, -1):
        x = kuyruk[i - 1].xcor()
        y = kuyruk[i - 1].ycor()
        kuyruk[i].goto(x, y)


    if len(kuyruk) > 0:
        x = bas.xcor()
        y = bas.ycor()
        kuyruk[0].goto(x, y)

    hareket()


    for segment in kuyruk:
        if segment.distance(bas) < 20:
            time.sleep(1)
            bas.goto(0, 0)
            bas.direction = "stop"


            if skor > topscore:
                topscore = skor


            skor = 0
            delay = 0.1

            for segment in kuyruk:
                segment.goto(1000, 1000)
            kuyruk.clear()

            kalem.clear()
            kalem.write("SKOR : {} TOP SKOR : {}".format(skor, topscore), align="center", font=("candara", 20, "bold"))

    time.sleep(delay)


pencere.bye()
