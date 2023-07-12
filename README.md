# 8 Queens Problem Solver with Genetic Algorithm

This project is a Python implementation of a solver for the 8 Queens Problem using a Genetic Algorithm. The 8 Queens Problem is a classic puzzle that involves placing 8 queens on an 8x8 chessboard in such a way that no two queens threaten each other. The Genetic Algorithm is an optimization technique inspired by the process of natural selection and genetics.

## Getting Started

To use this 8 Queens Problem solver, follow the instructions below:

1. Make sure you have Python 3 installed on your system.
2. Clone this repository to your local machine or download the source code files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Once the dependencies are installed, you can run the program by executing the following command:

   ```shell
   python main.py
   ```

## Usage

When you run the program, it will start solving the 8 Queens Problem using a genetic algorithm. The algorithm will evolve a population of solutions over generations to find an arrangement of queens that satisfies all the constraints.

The program will display the progress of each generation, including the fitness score. The fitness score represents the number of conflicts (threats) between the queens. The lower the score, the better the solution.

Once the program finds a solution with a fitness score of 28, it means the problem is solved, and the program will display the final arrangement of queens on the chessboard.

## Algorithm

This 8 Queens Problem solver uses a Genetic Algorithm, which is a heuristic search algorithm inspired by the process of natural selection and genetics. The algorithm works as follows:

1. **Initialization**: Create an initial population of random solutions, where each solution represents an arrangement of queens on the chessboard.
2. **Evaluation**: Calculate the fitness score for each solution in the population, representing the number of conflicts (threats) between the queens.
3. **Selection**: Select a subset of solutions from the population based on their fitness scores, giving higher chances to better solutions.
4. **Crossover**: Perform crossover (recombination) between pairs of selected solutions to create new offspring solutions. Crossover combines the characteristics of two solutions to generate new solutions.
5. **Mutation**: Apply random changes (mutations) to the offspring solutions to introduce new genetic material into the population.
6. **Replacement**: Replace a portion of the old population with the new offspring solutions.
7. **Termination**: Repeat steps 2 to 6 for a fixed number of generations or until a solution with a fitness score of 0 (no conflicts) is found.

By iterating through the steps of the genetic algorithm, the program progressively improves the solutions and converges towards a valid solution for the 8 Queens Problem.

## Example

Here are a few example of the output from running the program:

```
************* ITERATION: 14523 *************
[ 6, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 6, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 5, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 6, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 6, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 6, 2, 7, 5, 8, 8, 6, 3,  fitness = 27]
[ 4, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 6, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]

---------------- PADRES ----------------
[ 5, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]
[ 4, 2, 7, 5, 1, 8, 6, 3,  fitness = 27]

---------------- HIJOS -----------------
[ 5, 2, 7, 5, 1, 8, 6, 3,  fitness = 25]
[ 4, 2, 7, 5, 1, 8, 6, 3,  fitness = 28]


############### SOLUCION ################
[ 4, 2, 7, 5, 1, 8, 6, 3,  fitness = 28]


+  a  b  c  d  e  f  g  h
1  _  _  _  _  Q  _  _  _
2  _  Q  _  _  _  _  _  _
3  _  _  _  _  _  _  _  Q
4  Q  _  _  _  _  _  _  _
5  _  _  _  Q  _  _  _  _
6  _  _  _  _  _  _  Q  _
7  _  _  Q  _  _  _  _  _
8  _  _  _  _  _  Q  _  _

```
