import typing
import HighScoreManager
import Gui
from Board import Board
from Card import Card

class GameController:
    def __init__(self, board, gui, attempts, selection) -> None:
        self.board = Board
        self.gui = Gui
        self.attempts = attempts
        self.selection = selection

    def checkMatch(c1: Card, c2: Card) -> bool:
        return c1.getText() == c2.getText()

    def hasWon():
        return Board.isGameOver()
    
    



