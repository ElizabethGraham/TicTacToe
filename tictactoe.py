class TicTacToe:

    def __init__(self):
        self.xTurn = True
        self.turn_count = 0
        self.win_flag = False
        self.quit_flag = False
        self.game_pieces = ['X', 'O']
        self.coordinates = {"a1": 0, "b1": 1, "c1": 2,  # The coordinates and their respective move_list indices
                            "a2": 3, "b2": 4, "c2": 5, 
                            "a3": 6, "b3": 7, "c3": 8}
        self.lines = ["   a     b     c\n",
                      "      |     |     \n",
                      "1  {}  |  {}  |  {}  \n",  # Line 2
                      " _____|_____|_____\n",
                      "      |     |     \n",
                      "2  {}  |  {}  |  {}  \n",  # Line 5
                      " _____|_____|_____\n",
                      "      |     |     \n",
                      "3  {}  |  {}  |  {}  \n",  # Line 8
                      "      |     |    "]

        self.move_list = {0: "-", 1: "-", 2: "-",  # Where we store which game pieces are store on which spaces (Ex. [(3, x)]). Default is '-'
                          3: "-", 4: "-", 5: "-",
                          6: "-", 7: "-", 8: "-"}

    def main(self):
        while True:
            if self.quit_flag or self.win_flag:
                break  # If the user decided to quit, break the loop.

            self.print_board()  # Print out the ASCII board and current state
            self.take_move_input()  # Take the move input from user
            self.turn_count += 1
            if self.turn_count >= 5:  # After a win is possible...
                self.check_win()  # ...Check if a win condition has been met
            self.xTurn = not self.xTurn  # Change the turn
            
            

    def take_move_input(self):
        '''
            Moves should be inputted in a coordinate format, like (A1 = Top left, C3 = Bottom Right)
        '''

        current_move = input("Enter move coordinates: ")

        if (current_move == 'quit'):
            print ("User wants to quit")
            self.quit_flag = True
        else:
            if (current_move.lower() in self.coordinates):
                if self.move_list[self.coordinates[current_move]] == "-":
                    if self.xTurn:
                        self.move_list[self.coordinates[current_move]] = self.game_pieces[0]
                        self.print_board()  # Update the board
                    else: 
                        self.move_list[self.coordinates[current_move]] = self.game_pieces[1]
                        self.print_board()  # Update the board
                else:
                    print("That space has already been played. Try again.")
                    input("Press enter to continue...")
                    self.main()
            else:
                print("Can't find those coordinates. Try again.")
                input("Press enter to continue...")
                self.main()
        
        

    def print_board(self):
        '''
            For each line with game spaces, 
        '''
        for i in range(len(self.lines)):
            if (i == 2 or i == 5 or i == 8):
                print(self.lines[i].format(self.move_list.get(i-2), self.move_list.get(i-1), self.move_list[i]))
            else:
                print(self.lines[i])


    def check_win(self):
        '''
            Determine if a win condition has been met
        '''
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]  # All possible win conditions
        
        for idx, tup in enumerate(win_conditions):
            if self.move_list[tup[0]] in self.game_pieces and self.move_list[tup[0]] == self.move_list[tup[1]] and self.move_list[tup [1]] == self.move_list[tup[2]]:
                self.win_flag = True
                print("Game has been won")
                break
            else:
                pass

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.main()