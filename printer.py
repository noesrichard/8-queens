from board import Board
class Printer:

    def __init__(self) -> None:
        self.board_to_print = self.__generate_blank_board()

    def __generate_blank_board(self):
        # Generacion de una tabla en blanco 
        board_to_print = []
        for i in range(9):
            row = []
            if i == 0:
                for j in "abcdefgh":
                    if j == "a":
                        row.append(f"+  {j}")
                    else:
                        row.append(f" {j}")
                board_to_print.append(row)
            else: 
                for j in range(9):
                    if j == 0:
                        row.append(f"{i} ")
                    else: 
                        row.append("_ ")
                board_to_print.append(row)
        return board_to_print



    def print_board(self, board: Board):
        self.board_to_print = self.__generate_blank_board()
        for i in range(8):
            self.board_to_print[board.queens[i]][i+1] = "Q "

        print(board)
        print("\n")
        for i in range(len(self.board_to_print)):
            for j in range(len(self.board_to_print[i])):
                print(self.board_to_print[i][j], end=" ")
            print("")
        print("\n")


