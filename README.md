# Tower_of_Hanoi_Game

## Rules
The goal is to move all the disks from one rod to another rod without violating the sequence of arrangement. 
A few rules to be followed for Tower of Hanoi are the following:
- Only one disk can be moved among the rods at any given time.
- Only the "top" disk can be moved.
- No large disk can sit over a small disk.

## Algorithm

#### For 3 Rods
The Tower of Hanoi Game with n number of disks and **3** rods could result in a minimal number of moves of **2<sup>n</sup> - 1**
using the following strategy:
- Step 1: Move n-1 disks from source rod to aux rod
- Step 2: Move n<sup>th</sup> disk from source rod to dest rod
- Step 3: Move n-1 disks from aux rod to dest rod


#### For 4 Rods
The Tower of Hanoi Game with n number of disks and **4** rods could result in a minimal number of moves

<img src="https://latex.codecogs.com/png.image?\dpi{50}&space;\bg_black&space;&space;M(n)&space;=\begin{cases}1&space;&&space;n&space;=&space;1\\2&space;*&space;M(n-i)&space;&plus;&space;2^i&space;-&space;1&space;&&space;otherwise\end{cases}&space;" title="\bg_black M(n) =\begin{cases}1 & n = 1\\2 * M(n-i) + 2^i - 1 & otherwise\end{cases} " />

<img src="https://latex.codecogs.com/png.image?\dpi{80}&space;&space;M(n)&space;=\begin{cases}1&space;&&space;n&space;=&space;1\\2&space;*&space;M(n-i)&space;&plus;&space;2^i&space;-&space;1&space;&&space;otherwise\end{cases}&space;" title=" M(n) =\begin{cases}1 & n = 1\\2 * M(n-i) + 2^i - 1 & otherwise\end{cases} " />

using the following strategy:
- Step 1: Move the smallest d-k disks from rod 0 to rod 1, using all 4 rods.
- Step 2: Move the largest k disks from rod 0 to rod 3, without using rod 1. (In other words, move these disks using the optimal 3-rod method,
which is already known.)
- Step 3: Move the smallest d-k disks from rod 1 to rod 3, using all 4 rods.


Denoting by T(d, r) the minimal number of moves for a d-disk problem
on r rods, we see that the above method implies a recursive solution:

```equation
T(d, 4) = 2 ∗ T(d − k, 4) + T(k, 3)
```

Analysis of this recursion results in a closed-form solution for the minimizing value of k.

## Files
- Models
  - disk_model.py &rarr; Disk
  - move_sequence_model.py &rarr; MoveSequence
  - tohg_model.py &rarr; ToHG
  

- Controllers
  - console_controller.py
  - gui_viewables.py
  - gui_controller.py
  - gui_solution_controller.py
  - game_controller.py


## Reference
- [Original souce code](https://pythonturtle.academy/tower-of-hanoi/) for gui_solution_controller.py
