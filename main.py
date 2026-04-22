import tkinter as tk
import Board
import Game

def main():
    diff = {
        "easy": (2,2),
        "medium": (4,3),
        "hard":(4,4)
    }

    while True:
        userInput = input("select Difficulty")
        if userInput.lower().strip() in diff.keys():
            break
    
    rows, cols = diff[userInput]

    board = Board(rows, cols)
    board.loadWords("ordlista.txt")

    app = Game(board, dbPath="Highscores.pkl", mode=userInput)
    app.root.mainloop()

if __name__ == "__name__":
    main()
    

    