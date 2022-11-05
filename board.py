from random import randrange
class Board:
    def __init__(self, queens: list[int]) -> None:
        self.queens = queens
        self.fitness_score = self.__fitness_score()

    def __calculate_attacks(self):
        attacks = 0
        y_b = 0
        for y_a in range(len(self.queens)):
            x_a = self.queens[y_a]

            for y_b in range(y_a + 1, len(self.queens)):
                x_b = self.queens[y_b]

                if self.row_attack(x_a, x_b):
                    attacks += 1
                elif self.diagonal_attack(x_a, y_a, x_b, y_b):
                    attacks += 1

        return attacks

    def row_attack(self, x_a, x_b):
        return x_a == x_b

    def diagonal_attack(self, x_a, y_a, x_b, y_b):
        return (abs((y_b - y_a) / (x_b - x_a)) == 1 )

    def __fitness_score(self):
        return 28 - self.__calculate_attacks()

    def __str__(self) -> str:
        text = "[ "
        for i in self.queens:
            text += str(i)
            text += ", "
        text += f" fitness = {self.fitness_score}]"
        return text

    @classmethod
    def generate_board(cls):
        return Board([ randrange(0,8) for _ in range(8)])