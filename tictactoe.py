
# print("   a     b     c\n    |     |     \n1  -  |  -  |  -  \n _____|_____|_____\n      |     |     \n2  -  |  -  |  -  \n _____|_____|_____\n      |     |     \n3  -  |  -  |  -  \n      |     |    ")
lines = ["   a     b     c\n",
         "      |     |     \n",
         "1  {}  |  {}  |  {}  \n",  # Line 2
         " _____|_____|_____\n",
         "      |     |     \n",
         "2  {}  |  {}  |  {}  \n",  # Line 5
         " _____|_____|_____\n",
         "      |     |     \n",
         "3  {}  |  {}  |  {}  \n",  # Line 8
         "      |     |    "]

move_list = {0: "-", 1: "-", 2: "-",  # Where we store which game pieces are store on which spaces (Ex. [(3, x)]). Default is '-'
            3: "-", 4: "-", 5: "-",
            6: "-", 7: "-", 8: "-"}

coordinates = {"a1": 0, "b1": 1, "c1": 2,  # The coordinates and their respective move_list indices
               "a2": 3, "b2": 4, "c2": 5, 
               "a3": 6, "b3": 7, "c3": 8}
xTurn = True  # Will alternate between true and false. True = xTurn, False = yTurn
gamePieces = ['x', 'y']
winFlag = False  # False until a win is detected
quitFlag = Fals e

def main():
    while True:
        if (quitFlag):
            break  # If the user decided to quit, break the loop.

        print_board(move_list)  # Print out the ASCII board and current state
        take_move_input()  # Take the move input from user
        check_win()  # Check if a win condition has been met
        xTurn = not xTurn  # Change the turn
        
        

def take_move_input():
    '''
        Moves should be inputted in a coordinate format, like (A1 = Top left, C3 = Bottom Right)
    '''
    global quitFlag
    current_move = input("Enter move coordinates: ")

    if (current_move == 'quit'):
        print ("User wants to quit")
        quitFlag = True
    else:
        if (current_move.lower() in coordinates):
            if move_list[coordinates[current_move]] == "-":
                if xTurn:
                    move_list[coordinates[current_move]] = gamePieces[0]
                else: 
                    move_list[coordinates[current_move]] = gamePieces[1]
            else:
                print("That space has already been played. Try again.")
                input("Press enter to continue...")
                main()
        else:
            print("Can't find those coordinates. Try again.")
            input("Press enter to continue...")
            main()
    
    

def print_board(moves):
    '''
        For each line with game spaces, 
    '''
    for i in range(len(lines)):
        if (i == 2 or i == 5 or i == 8):
            print(lines[i].format(move_list.get(i-2), move_list.get(i-1), move_list[i]))
        else:
            print(lines[i])


def check_win():
    '''
        Determine if a win condition has been met
    '''
    global winFlag
    #diagonals = [(0,4,8), (2,4,6)]
    #across = [(0,1,2), (3,4,5), (6,7,8)]
    #uprights = [(0,3,6), (1,4,7), (2,5,8)]
    win_conditions = {(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8)(0,4,8), (2,4,6)}  # All possible win conditions

    for ind, tup in win_conditions:
        if tup[0] in gamePieces and tup[0] == tup[1] and tup [1] == tup[2]:
            winFlag = True
            print("Game has been")
        pass
    print("No Win Yet")

if __name__ == '__main__':
    main()