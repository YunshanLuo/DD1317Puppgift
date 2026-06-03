import tkinter as tk
from Board import Board
from Game import Game

def main():
    diff = {
        "easy": (2,2),
        "medium": (4,3),
        "hard":(4,4)
    }

    while True:
        userInput = input("Select difficulty (easy, medium, hard): \n").lower().strip()
        if userInput in diff:
            break
        else:
            print("Vänligen skriv (easy, medium eller hard)\n")
    
    rows, cols = diff[userInput]

    board = Board(rows, cols)
    board.loadWords("ordlista.txt")

    app = Game(board, dbPath="Highscores.pkl", mode=userInput)
    app.root.mainloop()

if __name__ == "__main__":
    main()
    

    