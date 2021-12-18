# Conways_Game_of_Life
### What Is Conway’s Game Of Life?
Conway’s Game of Life is a simulation which was (I believe) originally conceived by John Von Neumann as a model for self replicating robots. While Von Neumann found a solution to the problem, his answer was highly complicated. Conway’s contribution was to drastically simplify Von Neumann’s model so that it was governed by only four extremely simple rules, which I will list in a moment

The game is played on a grid of cells. Cells in this grid are either dead or alive (students will note
that this can easily be represented using a 2D array of Booleans or similar). In the picture below,
white squares are dead cells and blue squares are living cells.

Before the game begins, players can select which squares
start the game in a living state and which squares are dead.
(Hint: Take it as a 2D array of value 0/1, I will give this as
input. 1 is living state and 0 is dead state)

The game plays out in a sequence of turns. On each turn, the
program examines the state of every cell and applies four
rules to determine how the state of each cell will change. The
##### Rules are:
1. Any living cell which has less than two living
neighbours (up/down, left/right and diagonals) will die
of loneliness.
2. Any living cell which has more than three living
neighbours dies of starvation due to a lack of
sufficient resources.
3. Any dead cell with exactly three living neighbours will come to life through reproduction.
4. All other cells are unaffected. 

For every turn, the neighbours of every cell are counted, the counts of neighbours are tested with
these four rules and the state of each cell is updated accordingly. The program loops indefinitely
applying these rules and changing its state until the player decides to quit.

### Write a python script to take the following 2D matrix (1 – living, 0 – dead) as input and prints the output matrix after 20 turns of the game.
#### Input:
##### `0, 0, 1, 0, 1`
##### `0, 1, 0, 0, 1`
##### `0, 1, 0, 0, 1`
##### `0, 0, 1, 0, 1`
#### You are expected to print a 2D matrix following the same style after simulating the game for 20 turns.
