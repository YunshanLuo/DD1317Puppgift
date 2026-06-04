import tkinter as tk
from HighScoreManager import HighScoreManager
from Board import Board
from tkinter import messagebox

class Game(HighScoreManager):
    """
    The game class containing all necessary methods to make the game run
    """
    
    def __init__(self, board: Board, mode:str, dbPath = "Highscores.pkl"):
        """
        Inherits highscore manager in order to save directly into database
        Initializes class variables and calls setup
        """
        super().__init__(dbPath)
        
        self.root = tk.Tk()
        self.board = board
        self.mode = mode

        self.buttons = []
        self.firstCard = None
        self.firstButton = None
        self.isWaiting = False
        self.currScore = 0

        self.setUp()

    def setUp(self):
        """
        Places cards and loads score, uses a nested for loop to initialize buttons
        Button are stored in self.button and mapped with onclick lambda
        """
        self.root.title("Memory Game")
        self.board.placeCards()
        self.loadScore()

        for row in range(self.board.rows):
            buttonRow = []
            for col in range(self.board.columns):
                button = tk.Button(self.root,
                                   text="",
                                   width=5,
                                   height=5,
                                   command=lambda r = row, c = col: self.onClick(r, c))
                button.grid(row = row, column = col, padx = 3, pady= 3)
                buttonRow.append(button)
            self.buttons.append(buttonRow)

    def onClick(self, row, col):
        """
        Args (int):
            row: The clicked button row
            col: The clicked button column

        """
        # Handle spamming buttons
        if self.isWaiting:
            return
        
        clickedCard = self.board.getCard(row, col)
        clickedButton = self.buttons[row][col]

        # Nothing happens if you click already matched card or the same card again
        if clickedCard.isMatched or clickedCard == self.firstCard:
            return
        
        # Display card word
        clickedButton.config(text = str(clickedCard))

        # If first time clicking set firstCard = None        
        if self.firstCard is None:
            self.firstCard = clickedCard
            self.firstButton = clickedButton
        else:
            self.currScore += 1
            # Matched
            if self.board.checkMatch(self.firstCard, clickedCard):
                self.firstButton.config(state="disabled")
                clickedButton.config(state="disabled")

                self.firstCard = None
                self.firstButton = None
                self.checkWin()
            else:
            # Not matched
                self.isWaiting = True  # Set isWaiting to true to disallow spamming
                self.root.after(500, lambda b1=self.firstButton, b2=clickedButton: self.hideCards(b1, b2))
                self.firstCard = None
                self.firstButton = None
    
    def hideCards(self, button1, button2):
        button1.config(text="")
        button2.config(text="")
        self.isWaiting = False
    

    def checkWin(self):
        # If all cards isMatched
        if self.board.isGameOver():
            # All parent method
            self.addScore(self.mode, self.currScore)
            rank = self.getRank(self.mode, self.currScore)

            messagebox.showinfo("Grattis!", f"Du vann med {self.currScore} drag och din rank är #{rank}")
            self.root.destroy()