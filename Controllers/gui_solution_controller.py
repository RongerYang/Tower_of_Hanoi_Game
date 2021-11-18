"""
A GUI Solution Controller for Tower of Hanoi Game with number of rods = 3

reference source:
https://pythonturtle.academy/tower-of-hanoi/

=== Attributes ===
    @param int _num_disks: the number of disks
    to run this GUISolutionController
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

    """
    Initialize a GUISolutionController.

    @param GUISolutionController self: this GUISolutionController self
    @param int num_disks: the number of disks
    @rtype: None
    """
    def __init__(self, num_disks):
        self._num_disks = num_disks
        # global ring_width_max, ring_width_min, ring_ratio, ring_delta

    """
    Draw lines to this GUISolutionController.
    
    @param GUISolutionController self: this GUISolutionController self
    @param float x: x-coordinate to start drawing
    @param float y: y-coordinate to start drawing
    @param float heading: angle to heading
    @param float length: distance to move forward
    @param float pensize: size of the pen
    @param str color: color of the line
    @rtype: None
    """
    def draw_line(self, x, y, heading, length, pensize, color):
        turtle.up()
        turtle.goto(x, y)
        turtle.seth(heading)
        turtle.down()
        turtle.color(color)
        turtle.pensize(pensize)
        turtle.fd(length)

    """
    Draw scenes to this GUISolutionController.

    @param GUISolutionController self: this GUISolutionController self
    @rtype: None
    """
    def draw_scene(self):
        turtle.bgcolor('light blue')
        self.draw_line(-600, -100, 0, 1200, 10, 'brown')
        for i in range(-250, 251, 250):
            self.draw_line(i, -93, 90, peg_height, 5, 'black')

    """
    Draw a single ring to this GUISolutionController.

    @param GUISolutionController self: this GUISolutionController self
    @param float r: radius of the ring
    @param float x: x-coordinate to start drawing
    @param float k: 
    @param float extra: 
    @rtype: None
    """
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

    """
    Draw rings to this GUISolutionController.

    @param GUISolutionController self: this GUISolutionController self
    @rtype: None
    """
    def draw_rings(self):
        for i in range(len(A)):
            self.draw_single_ring(A[i], -250, i)
        for i in range(len(B)):
            self.draw_single_ring(B[i], 0, i)
        for i in range(len(C)):
            self.draw_single_ring(C[i], 250, i)

    """
    Redraw and move the ring position.
    
    @param GUISolutionController self: this GUISolutionController self
    @param str source: 
    @param str dest: 
    @rtype: None
    """
    def move_ring(self, source, dest):
        if source == "A":
            x = -250
            P = A
        elif source == "B":
            x = 0
            P = B
        else:
            x = 250
            P = C

        if dest == "A":
            x2 = -250
            Q = A
        elif dest == "B":
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


    """
    Move rings in source to dest
    
    @param GUISolutionController self: this GUISolutionController self
    @param str source: source rod
    @param str aux: auxiliary rod
    @param str dest: destination rod
    @param int n: number of disks
    @rtype: None
    """
    def tower_of_hanoi(self, source, aux, dest, n):
        if n == 1:
            self.move_ring(source, dest)
            return
        self.tower_of_hanoi(source, dest, aux, n - 1)
        self.move_ring(source, dest)
        self.tower_of_hanoi(aux, source, dest, n - 1)

    """
    Start this GUISolutionController.
    
    @param GUISolutionController self: this GUISolutionController self
    @rtype: None
    """
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