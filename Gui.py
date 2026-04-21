import tkinter as tk
import HighScoreManager
import Board

class Game:
    def __init__(self, board: Board, manager: HighScoreManager):
        self.root = tk.Tk()
        self.board = board
        self.manager = manager

        self.buttons = []
        self.firstCard = None
        self.firstButton = None
        self.isWaiting = False

        self.setUp()

    def setUp(self):
        self.root.title("Memory Game")
        self.board.placeCards()
        self.manager.loadScores()

        for row in range(self.board.rows):
            buttonRow = []
            for col in range(self.board.columns):
                button = tk.Button(self.root,
                                   text="",
                                   width=4,
                                   height=4,
                                   command=lambda: self.onClick(row, col))
                button.grid(row = row, column = col, padx = 3, pady= 3)
                buttonRow.append(button)
            self.buttons.append(buttonRow)

    def onClick(self, row, col):
        if self.isWaiting:
            return
        
        clickedCard = self.board.getCard(row, col)
        clickedButton = self.buttons[row][col]

        if clickedCard.isMatched or clickedCard == self.firsCard:
            return
        
        clickedButton.config(text = str(clickedCard))
        
        if self.firstCard is None:
            self.firstCard = clickedCard
            self.firstButton = clickedButton
        else:
            self.manager.currScore += 1
            # Matched
            if self.board.checkMatch(self.firstCard, clickedCard):
                self.firstButton.config(state="disabled")
                clickedButton.config(state="disabled")

                self.firstCard = None
                self.firstButton = None
                self.checkWin()
            else:
            # Not matched
                self.isWaiting = True
                self.root.after(2000, lambda: self.hideCards(self.firstButton, clickedButton))
                self.firstCard = None
                self.firstButton = None
    
    def hideCards(self, button1, button2):
        button1.config(text="")
        button2.config(text="")
        self.isWaiting = False
        