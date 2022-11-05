from random import randrange, shuffle
from board import Board
MAX_POPULATION = 8
MUTATION_RATE = 5

def generate_population():
    population = [ Board.generate_board() for _ in range(MAX_POPULATION)]
    population.sort(key=lambda x: x.fitness_score, reverse=True)
    return population

def select_parents(population: list[Board]):
    total_score = 0
    for ind in population:
        total_score += ind.fitness_score

    bag = []
    for ind in population:
        percentage = (ind.fitness_score / total_score) * 100
        for _ in range(round(percentage)):
            bag.append(ind)

    shuffle(bag)
    father: Board = bag[randrange(0,len(bag))]
    mother: Board = bag[randrange(0,len(bag))]
    while father == mother:
        mother: Board = bag[randrange(0,len(bag))]

    print(f"****************** AVERAGE SCORE : {total_score/len(population)} ****************** ")

    return father, mother

def crossover(father: Board, mother: Board):
    cut = randrange(0,8)
    print(cut)
    child_one_queens: list[int] = father.queens[:cut] + mother.queens[cut:]
    child_two_queens: list[int] = mother.queens[:cut] + father.queens[cut:]

    child_one = Board(child_one_queens)
    child_two = Board(child_two_queens)

    return child_one, child_two

def mutation(child: Board):
    if randrange(0, 100) <= 5:
        child.queens[randrange(0,8)] = randrange(0, 8)
        return True
    return False

def is_solved(population: list[Board]):
    for ind in population:
        if ind.fitness_score == 28:
            return True
    return False


def main():
    population = generate_population()
    i = 0
    best_score = 0

    while not is_solved(population) or i <= 2000:
        i += 1
        print(f"\n****************** ITERATION: {i} ******************")

        for ind in population:
            print(ind)
            if ind.fitness_score > best_score:
                best_score = ind.fitness_score

        father, mother = select_parents(population)

        print("\n------------ PARENTS -----------")
        print(father)
        print(mother)

        child_one, child_two = crossover(father, mother)


        print("\n------------ CHILDREN -----------")
        print(child_one)
        print(child_two)

        if mutation(child_one):
            print(child_one)
        elif mutation(child_two):
            print(child_two)

        population.remove(father)
        population.remove(mother)

        population.append(child_one)
        population.append(child_two)

        print(f"BEST SCORE : {best_score}")

    board_to_print =  [['_' for _ in range(8)] for _ in range(8)]
    for ind in population: 
        if ind.fitness_score == 28:
            for i in range(8):
                board_to_print[i][ind.queens[i]] = 'Q'

    for i in range(len(board_to_print)):
        for j in range(len(board_to_print[i])):
            print(board_to_print[i][j], end=' ')
        print("")



if __name__ == "__main__":
    main()
