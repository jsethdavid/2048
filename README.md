# 2048
2048 is a single-player sliding block puzzle game. The game's
objective is to slide numbered tiles on a grid to combine them to
create a tile with the number 2048. Every turn, a new tile will
randomly appear in an empty spot on the board with a value of
either 2 or 4. Tiles slide as far as possible in the chosen direction
until they are stopped by either another tile or the edge of the grid.
If two tiles of the same number collide while moving, they will
merge into a tile with the total value of the two tiles that collided.
The resulting tile cannot merge with another tile again in the same
move.

This assignment uses a simplified version of the 2048 Game where the goal can be set to a value
different from 2048. In this version the new tile is always a 2, and appears in the first available position
from the row or column opposite to the last movement. The game implementation is provided in the file
“game.py”. The “main” method in this file allows to play the game given the input entries of a human
player through the command line.
A file named “algorithms.py” provides an implementation of A* that uses the game board and a user
defined heuristic to search the solution tree. The A* algorithm runs until a sequence of actions is found
that achieves the goal. Running the “main” method starts the A* algorithm; after a successful path is
found, the path, its length, and the required computational time are printed. If the heuristic is poor or
the game settings are too difficult the algorithm may not end on a reasonable time or produce an “out
of memory” exception.

The goal is to design, code and test different heuristics for the 2048 Game. Every heuristic that achieves
a better result than the number of tiles heuristics can be reported. The grade will depend on the
amount and quality of the reported heuristics. To report each heuristic a pdf document should be
submitted explaining the logic behind the heuristic and the implemented code. It is also recommended
to add the achieved times for different game configurations.
