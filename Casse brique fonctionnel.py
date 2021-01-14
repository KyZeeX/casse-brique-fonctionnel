import random
import pygame
import core
from pygame.locals import *
pygame.init()
hauteur = 800
largeur = 600

vie = 4
briquel1 = []
briquel2 = []
briquel3 = []
briquel4 = []
raquette = []
balls = []


def setup():
    pygame.init()
    print("setup")
    global score,briquel1, briquel2, briquel3, briquel4, x, y, l, h, xd, yd, balls, raquette,X,Y,X1,Y1,L,H

    core.WINDOW_SIZE = [largeur, hauteur]
    core.fps=30

    for b1 in range(0,10) :

        l = 60
        h = 20
        x = 1
        y = 1
        briquel1 = briquel1 + [[x*(b1-1)+(l*b1), y, l, h,]]
    for b2 in range(0, 10):
            l = 60
            h = 20
            x = 1
            y = 1
            briquel2 = briquel2 + [[x * (b2 - 1) + (l * b2), y*h+2, l, h, ]]
    for b3 in range(0, 10):
            l = 60
            h = 20
            x = 1
            y = 1
            briquel3 = briquel3 + [[x * (b3 - 1) + (l * b3), 2*y*h+3, l, h, ]]
    for b4 in range(0, 10):
            l = 60
            h = 20
            x = 1
            y = 1
            briquel4 = briquel4 + [[x * (b4 - 1) + (l * b4), 3*y*h+4, l, h, ]]
    for i in range(0,1):
        L=80
        H=20
        XR=260
        YR=700
        raquette = raquette + [[XR,YR,L,H]]

    X = 300
    Y = 550

    xd = random.uniform(-10, 10)
    yd = random.uniform(-10, 10)
    balls = balls + [X, Y, xd, yd,]
    score = 0
    print("Une partie débute, vous avez", vie,"vie(s) pour terminer le casse brique")

def Spring(b1,b2,k,lo):
    u = pygame.Vector2(b2[0] - b1[0], b2[1] - b1[1])
    distanceEntreB1etB2 = u.length()

    if u[0] == 0 and u[1]==0:
        return [0,0]

    u = u.normalize()

    Fx = u[0] * k * abs(distanceEntreB1etB2  - lo)
    Fy = u[1] * k * abs(distanceEntreB1etB2  - lo)

    return [Fx,Fy]

def run():
    global score,q1,q2,q3,q4

    for q in briquel1:

        pygame.draw.rect(core.screen,(255, 0, 0), (q[0], q[1], q[2], q[3]))

    for q2 in briquel2 :
        pygame.draw.rect(core.screen, (255, 0, 0), (q2[0], q2[1], q2[2], q2[3]))

    for q3 in briquel3:
        pygame.draw.rect(core.screen, (255, 0, 0), (q3[0], q3[1], q3[2], q3[3]))

    for q4 in briquel4:
        pygame.draw.rect(core.screen, (255, 0, 0), (q4[0], q4[1], q4[2], q4[3]))

    for r in raquette:

        pygame.draw.rect(core.screen, (255, 0, 0), (r[0], r[1], r[2], r[3]))

    pygame.draw.circle(core.screen, (36, 210, 78), (balls[0], balls[1]), 20)

    balls[0] = balls[0] + balls[2]
    balls[1] = balls[1] + balls[3]

    if balls[0] < 20 or balls[0] > largeur - 20:
            balls[2] = -balls[2]
    if balls[1] < 20:
            balls[3] = -balls[3]

    if balls[1] > hauteur :
        balls[1] = 250
        balls[0] = 250
        score = score +1
        print("il vous reste", vie - score, "vie(s)")

    if vie - score == 0 :
        print("game over")
        exit()

    for q4 in briquel4 :
        if q4[0] < balls[0] < q4[0] + l and q4[1] < balls[1] - 20 < q4[1]+h :
            balls[3] = - balls[3]
            briquel4.remove(q4)




    for q3 in briquel3:
        if q3[0] < balls[0] < q3[0] + l and q3[1] < balls[1] - 20 < q3[1] + h:
            balls[3] = - balls[3]
            briquel3.remove(q3)

    for q2 in briquel2:
        if q2[0] < balls[0] < q2[0] + l and q2[1] < balls[1] - 20 < q2[1] + h:
            balls[3] = - balls[3]
            briquel2.remove(q2)

    for q1 in briquel1:
        if q1[0] < balls[0] < q1[0] + l and q1[1] < balls[1] - 20 < q1[1] + h:
            balls[3] = - balls[3]
            briquel1.remove(q1)

    if briquel1 is not None and not briquel1 and briquel2 is not None and not briquel2 and briquel3 is not None and not briquel3 and briquel4 is not None and not briquel4:
        print("bravo tu as gagné")
        exit()


    if r[1] < balls[1] + 20 < r[1] + r[3] and r[0] <= balls[0] < r[0] + 20 :
            balls[3] = -balls[3]
            balls[2] = - balls[2]

    if r[1] < balls[1] + 20 < r[1] + r[3] and r[0] +20 <= balls[0] < r[0] + 60 :
            balls[3] = -balls[3]

    if r[1] < balls[1] + 20 < r[1] + r[3] and r[0] + 60 <= balls[0] < r[0] + r[2]:
        balls[3] = -balls[3]
        balls[2] = -balls[2]
    if core.getMouseLeftClick() is not None:
        if core.getMouseLeftClick()[0] < largeur - r[2] :
            r[0]=core.getMouseLeftClick()[0]

core.main(setup, run)