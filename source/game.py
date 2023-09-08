import time
from utils import draw_board, clear_screen, whose_turn, check_winner
from random import randint as random_int


class Game:
    def __init__(self):
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]
        self.player = ""

    def position_available(self, choice):
        if int(choice) <= 3:
            field_chosen = self.board[0][int(choice) - 1]
            if field_chosen == "_":
                self.board[0][int(choice) - 1] = self.player
                return True
            print("Invalid choice. Try again!")
        elif int(choice) <= 6:
            field_chosen = self.board[1][int(choice) - 4]
            if field_chosen == "_":
                self.board[1][int(choice) - 4] = self.player
                return True
            print("Invalid choice. Try again!")
        elif int(choice) <= 9:
            field_chosen = self.board[2][int(choice) - 7]
            if field_chosen == "_":
                self.board[2][int(choice) - 7] = self.player
                return True
            print("Invalid choice. Try again!")
        return False

    def computer_move(self):
        if "_" in self.board[0] or "_" in self.board[1] or "_" in self.board[2]:
            position = random_int(1, 9)

            if self.position_available(position):
                print(f"Computer taken place--> {position}")
            else:
                self.computer_move()

    def ask_verify_choice(self):
        while True:
            try:
                choice = int(input("Enter a position (1-9): "))
            except ValueError:
                print("Invalid choice. Try again!")
                continue
            except KeyboardInterrupt:
                print("\nBye!")
                exit(0)

            if self.position_available(choice):
                break

    def main_loop(self):
        for i in range(9):
            clear_screen()

            draw_board(self.board)

            self.player = whose_turn(i)

            if self.player == "O":
                self.computer_move()
            else:
                self.ask_verify_choice()

            did_win, self.board = check_winner(self.board)

            if did_win:
                clear_screen()
                draw_board(self.board)
                print(f"Player {self.player} wins!")
                time.sleep(2)
                break
