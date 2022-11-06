from board import Board
from random import randrange, shuffle

class EightQueenGA:

    def __init__(self) -> None:
        self.MAX_POPULATION = 8
        self.MUTATION_RATE = 25

        # Generacion de la poblacion inicial
        self.population = self.__generate_population()
        self.population.sort(key=lambda x: x.fitness_score, reverse=True)

        self.solution = None
        self.children = []

    def solve(self):
        i = 0
        while not self.__is_solved():

            #self.population.append(Board([7, 3, 8, 2, 5, 1, 6, 4]))

            # Imprimir individuos en la poblacion
            print(f"\n************* ITERATION: {i} *************")
            self.__print_individuos(*self.population)

            # Seleccion de padres
            father, mother = self.__select_parents()

            # Crossover, generacion de hijos
            child_one, child_two = self.__crossover(father, mother)

            # Mutacion de hijos
            self.__mutation(child_one, child_two)

            # Modificar la poblacion, para generar la proxima generacion
            self.__next_generation(child_one, child_two)


            # Imprimir padres
            print("\n---------------- PADRES ----------------")
            self.__print_individuos(father, mother)

            # Imprimir hijos
            print("\n---------------- HIJOS -----------------")
            self.__print_individuos(child_one, child_two)

            i += 1



    def __generate_population(self) -> list[Board]:
        # Generamos la poblacion inicial 
        population = [Board.generate_board() for _ in range(self.MAX_POPULATION)]
        population.sort(key=lambda x: x.fitness_score, reverse=True)
        return population

    def __select_parents(self):

        # Acumulacion total del puntaje de ajuste
        total_score = 0
        for ind in self.population:
            total_score += ind.fitness_score

        # Almacenamos todos los individuos segun su probabilidad en una "bolsa negra"
        bag = []
        for ind in self.population:
            # Calculo de la probabilidad de cada individuo 
            # Su probabilidad sera igual a su puntacion de ajuste sobre el ajuste total

            # Por lo que aquellos que tengan menor numero de ataques o lo que es igual
            # mayor puntuacion de ajuste tendran mas probabilidad de ser elegidos como
            # padres
            probability = (ind.fitness_score / total_score) * 100
            for _ in range(round(probability)):
                bag.append(ind)

        # Randomizamos la posicion de los individuos en la bolsa
        shuffle(bag)

        # Elejimos a los padres de una manera randomica
        father: Board = bag[randrange(0, len(bag))]
        mother: Board = bag[randrange(0, len(bag))]
        while father == mother:
            mother: Board = bag[randrange(0, len(bag))]

        return father, mother


    def __crossover(self, father: Board, mother: Board):
        # Punto de cruce o corte
        cut = randrange(0, 8)

        # Cruce de los genes
        child_one_queens: list[int] = father.queens[:cut] + mother.queens[cut:]
        child_two_queens: list[int] = mother.queens[:cut] + father.queens[cut:]

        # Generacion de dos hijos con dichos genes
        child_one = Board(child_one_queens)
        child_two = Board(child_two_queens)

        return child_one, child_two

    def __mutation(self, child_one, child_two):
        if randrange(0, 100) < self.MUTATION_RATE:
            if randrange(0,2) == 1:
                child_one.queens[randrange(0, 8)] = randrange(1, 9)
            else: 
                child_two.queens[randrange(0, 8)] = randrange(1, 9)


    def __next_generation(self,child_one, child_two):
        self.children.append(child_one)
        self.children.append(child_two)
        if len(self.children) == len(self.population):
            self.population = [ind for ind in self.children]
            self.children = []


    def __is_solved(self):
        for ind in self.population:
            if ind.fitness_score == 28:
                self.solution = ind
                return True
        return False

    def __print_individuos(self, *individuos: Board):
        for ind in individuos:
            print(ind)


