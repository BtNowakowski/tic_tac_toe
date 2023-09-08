import time
from utils import draw_board, clear_screen, check_winner
from random import choice as random_choice

PLAYER = "X"
COMPUTER = "O"
EMPTY = "_"


class Game:
    def __init__(self):
        self.board = [
            [EMPTY] * 3,
            [EMPTY] * 3,
            [EMPTY] * 3,
        ]
        self.player = ""
        self.free_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def whose_turn(self, turn):
        if turn % 2 == 0:
            return PLAYER
        return COMPUTER

    def take_position(self, choice):
        if int(choice) >= 1 and int(choice) <= 3:
            self.board[0][int(choice) - 1] = self.player
            self.free_spots.remove(int(choice))
        elif int(choice) >= 4 and int(choice) <= 6:
            self.board[1][int(choice) - 4] = self.player
            self.free_spots.remove(int(choice))
        elif int(choice) >= 7 and int(choice) <= 9:
            self.board[2][int(choice) - 7] = self.player
            self.free_spots.remove(int(choice))

    def computer_move(self):
        if self.free_spots:
            self.take_position(random_choice(self.free_spots))
        else:
            print("Thanks for playing!")
            exit(0)

    def player_move(self):
        while True:
            try:
                choice = int(input("Enter a position (1-9): "))
            except ValueError:
                print("Invalid choice. Try again!")
                continue
            except KeyboardInterrupt:
                print("\nBye!")
                exit(0)

            if choice in self.free_spots:
                break

        self.take_position(choice)

    def main_loop(self):
        for i in range(9):
            # board operations
            clear_screen()
            draw_board(self.board)

            self.player = self.whose_turn(i)

            if self.player == COMPUTER:
                self.computer_move()
            else:
                self.player_move()

            if i >= 5:
                did_win, self.board = check_winner(self.board)
                if did_win:
                    clear_screen()
                    draw_board(self.board)
                    print(f"Player {self.player} wins!")
                    time.sleep(2)
                    break
