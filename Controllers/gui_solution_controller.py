"""
A GUI Solution Controller for Tower of Hanoi Game with number of rods = 3
"""

import turtle
import colorsys
import math

turtle.setup(1000, 1000)
turtle.hideturtle()
turtle.title("Tower of Hanoi - GUI Solution")
turtle.speed(0)
turtle.tracer(0, 0)

# num_disks = 5
peg_height = 300
ring_height_max = 10
ring_width_max = 150
ring_width_min = 20
ring_delta = 15
ring_delta_max = 30
ring_height = 20
animation_step = 10

A = []  # List of rings in Peg A
B = []
C = []

T = []  # list of turtles

class GUISolutionController:

    def __init__(self, num_disks):
        self._num_disks = num_disks
        # global ring_width_max, ring_width_min, ring_ratio, ring_delta


    def draw_line(self, x, y, heading, length, pensize, color):
        turtle.up()
        turtle.goto(x, y)
        turtle.seth(heading)
        turtle.down()
        turtle.color(color)
        turtle.pensize(pensize)
        turtle.fd(length)


    def draw_scene(self):
        turtle.bgcolor('light blue')
        self.draw_line(-600, -100, 0, 1200, 10, 'brown')
        for i in range(-250, 251, 250):
            self.draw_line(i, -93, 90, peg_height, 5, 'black')


    def draw_single_ring(self, r, x, k, extra=0):
        global ring_delta
        w = ring_width_max - ring_delta * (r - 1)
        T[r].up()
        T[r].goto(x - w / 2, -95 + ring_height * k + extra)
        T[r].down()
        T[r].seth(0)
        T[r].begin_fill()
        for i in range(2):
            T[r].fd(w)
            T[r].left(90)
            T[r].fd(ring_height)
            T[r].left(90)
        T[r].end_fill()


    def draw_rings(self):
        for i in range(len(A)):
            self.draw_single_ring(A[i], -250, i)
        for i in range(len(B)):
            self.draw_single_ring(B[i], 0, i)
        for i in range(len(C)):
            self.draw_single_ring(C[i], 250, i)


    def move_ring(self, PP, QQ):
        if PP == "A":
            x = -250
            P = A
        elif PP == "B":
            x = 0
            P = B
        else:
            x = 250
            P = C

        if QQ == "A":
            x2 = -250
            Q = A
        elif QQ == "B":
            x2 = 0
            Q = B
        else:
            x2 = 250
            Q = C

        for extra in range(1, 250 - (-95 + ring_height * (len(P) - 1)), animation_step):
            T[P[len(P) - 1]].clear()
            self.draw_single_ring(P[len(P) - 1], x, len(P) - 1, extra)
            turtle.update()

        T[P[len(P) - 1]].clear()
        self.draw_single_ring(P[len(P) - 1], x, len(P) - 1, extra)
        turtle.update()
        tp = x
        if x2 > x:
            step = animation_step
        else:
            step = -animation_step
        for tp in range(x, x2, step):
            T[P[len(P) - 1]].clear()
            self.draw_single_ring(P[len(P) - 1], tp, len(P) - 1, extra)
            turtle.update()
        T[P[len(P) - 1]].clear()
        self.draw_single_ring(P[len(P) - 1], x2, len(P) - 1, extra)
        turtle.update()
        Q.append(P[len(P) - 1])
        del P[-1]
        for extra in range(250 - (-95 + ring_height * (len(Q) - 1)), 0, -animation_step):
            T[Q[len(Q) - 1]].clear()
            self.draw_single_ring(Q[len(Q) - 1], x2, len(Q) - 1, extra)
            turtle.update()
        T[Q[len(Q) - 1]].clear()
        self.draw_single_ring(Q[len(Q) - 1], x2, len(Q) - 1)
        turtle.update()
        return


    # move rings in X to Z
    def tower_of_hanoi(self, X, Y, Z, n):
        if n == 1:
            self.move_ring(X, Z)
            return
        self.tower_of_hanoi(X, Z, Y, n - 1)
        self.move_ring(X, Z)
        self.tower_of_hanoi(Y, X, Z, n - 1)

    def start_gui(self):
        self.draw_scene()
        turtle.update()
        for i in range(self._num_disks):
            A.append(i)
            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0)
            t.pencolor('red')
            t.fillcolor('light green')
            T.append(t)
        ring_delta = min(135 / (self._num_disks - 1), ring_delta_max)
        self.draw_rings()
        self.tower_of_hanoi("A", "B", "C", self._num_disks)
        turtle.update()



if __name__ == '__main__':
    num_disks = int(turtle.numinput('Number of Rings', 'Please enter number of rings:', 5, 2, 10))
    gsc = GUISolutionController(num_disks)
    gsc.start_gui()