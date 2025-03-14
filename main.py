import pgzrun
from random import randint


apple = Actor("apple")
banana = Actor("banana")
orange = Actor("orange")
pineapple = Actor("pineapple")

fruits = [apple,banana,orange,pineapple]
fruit = None
score = 0
Time = 15.5
messageG = ""
messageM = ""

def draw():
    screen.clear()
    if Time > 0:
        fruit.draw()
        screen.draw.text(f"Time left: {Time}", (10, 10), fontsize=40, color="white")
        screen.draw.text(f"Score: {score}", (670, 10), fontsize=40, color="white")
        if messageG:
            screen.draw.text(messageG, center=(400, 40), fontsize=50, color="green")
        elif messageM:
            screen.draw.text(messageM, center=(400, 40), fontsize=50, color="red")
    else:
        screen.draw.text("Game Over!", (300, 250), fontsize=60, color="red")
        screen.draw.text(f"Final Score: {score}", (300, 310), fontsize=50, color="white")


def place_fruit():
    global fruit
    fruit = fruits[randint(0, 3)]

    fruit.x = randint(70,600)
    fruit.y = randint(100,500)

def on_mouse_down(pos):
    global Time,score,messageG,messageM
    if fruit and Time > 0 and fruit.collidepoint(pos):
        score += 1
        Time += 0.5
        place_fruit()
        messageG = "Nice Shot!\n +0.5"
        clock.schedule_unique(clear_message, 0.2)

    else:
        Time -= 2
        messageM = "You missed!\n -2"
        clock.schedule_unique(clear_message, 0.2)

def clear_message():
    global messageG,messageM
    messageG = ""
    messageM = ""

def update_timer():
    global Time
    if Time > 0:
        Time -= 1

clock.schedule_interval(update_timer, 1.0)

place_fruit()

pgzrun.go()
