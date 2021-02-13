using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace TicTacToe
{
    class TicTacToe
    {
        bool xTurn = true;
        bool winFlag = false;
        bool quitFlag = false;

        public static List<string> gamePieces = new List<string>();
        gamePieces.Add("x");
        gamePieces.Add("y");

        public static List<string> gameBoard = new List<string>() {
            ["   a     b     c\n",
            "      |     |     \n",
            "1  {}  |  {}  |  {}  \n",  # Line 2
            " _____|_____|_____\n",
            "      |     |     \n",
            "2  {}  |  {}  |  {}  \n",  # Line 5
            " _____|_____|_____\n",
            "      |     |     \n",
            "3  {}  |  {}  |  {}  \n",  # Line 8
            "      |     |    "]
        };

        public static Dictionary<int, string> gameBoard = new Dictionary<int, string>() {
            {0: "-", 1: "-", 2: "-",
            3: "-", 4: "-", 5: "-",
            6: "-", 7: "-", 8: "-"}
        };


        public static void Main(string[] args)
        {
             while (true)
             {
                 if (quitFlag == true) 
                 {
                     break;
                 }

                 xTurn = !xTurn;
             }
        }

        public static void takeMoveInput() 
        {

        }


        public static void printBoard() 
        {

        }


        public static void checkWin()
        {

        }
    }
}