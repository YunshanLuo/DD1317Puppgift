from Card import Card
from typing import List
import random 

class Board:
    rows: int
    columns: int
    cards: List[Card]

    def __init__(self, rows: int, columns: int, cards: List[Card]) -> None:
        self.rows = rows
        self.columns = columns
        self.cards = cards
        

    def isGameOver(self) -> bool:
        """
        Check if all cards have been matched
        """
        for card in self.cards:
            if not card.isMatched:
                return False
        return True
    
    def getCard(self, row: int, col: int) -> Card:
        for card in self.cards:
            if card.atRow == row and card.atCol == col:
                return card
        return None
    
    def placeCards(self) -> None:
        random.shuffle(self.cards)
        idx = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if idx < len(self.cards):
                    card = self.cards[idx]
                    card.atRow = i
                    card.atCol = j
                    idx += 1


    

    
        

    

