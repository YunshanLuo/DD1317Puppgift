from Card import Card
from typing import int, List, str, bool
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
        for i in range(row):
            for j in range(col):
                if Card.atRow == j and Card.atCol == i:
                    return Card
    
    def placeCards(self) -> None:
        random.shuffle(self.cards)
        for i in range(self.rows):
            for j in range(self.columns):
                for card in self.cards:
                    card.atCol = i
                    card.atCol = j


    

    
        

    

