from algorithm import EightQueenGA
from printer import Printer

if __name__ == "__main__":
    printer = Printer()

    genetic_algorithm = EightQueenGA()

    genetic_algorithm.solve()

    print("\n\n############### SOLUCION ################")
    printer.print_board(genetic_algorithm.solution)
