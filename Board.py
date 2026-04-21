from Card import Card
from typing import List
import random 

class Board:
    rows: int
    columns: int
    cards: List[Card]

    def __init__(self, rows: int, columns: int, cards: List[Card]) -> None:
        """
        Initailizes the board with row, col and a set of cards
        
        Args:
            rows (int): The total number of rows
            columns (int): The total number of columns
            cards (List[Card]): List of Card objects to put on the board
        """
        self.rows = rows
        self.columns = columns
        self.cards = cards
        

    def isGameOver(self) -> bool:
        """
        Check isMatched attribute for all Cards on the board

        Returns (boolean):
            True if all cards are matched, False otherwise
        """

        for card in self.cards:
            if not card.isMatched:
                return False
        return True
    
    def getCard(self, row: int, col: int) -> Card:
        """
        Args:
            row (int): row the quered card is on 
            col (int): the column quered card is on 
        
        Returns:
            Card instance at (row, col)
        """
        for card in self.cards:
            if card.atRow == row and card.atCol == col:
                return card
        return None
    
    def placeCards(self) -> None:
        """
        Shuffles the list of cards and assigns each card an atRow, atCol value
        """
        random.shuffle(self.cards)
        idx = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if idx < len(self.cards):
                    card = self.cards[idx]
                    card.atRow = i
                    card.atCol = j
                    idx += 1
    
    def checkMatch(self, card1: Card, card2: Card) -> bool:
        """
        Check if two cards are matching by seeing if they have the same text

        Args:
            card1 (Card): The first comparable card
            card2 (Card): The second comparable card
        
        Returns:
            bool: True if the cards match, False otherwise
        """
        if str(card1) == str(card2):
            card1.isMatched = True
            card1.isMatched = True
            return True
        return False
    
            


    

    
        

    

