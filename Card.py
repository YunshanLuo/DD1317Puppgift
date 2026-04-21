
class Card:
    """
    Represents a card in Memory Game

    Attributes:
        word: Word stored on the card
        isFaceUp: True if card is visible to the player
        isMathced: True if card has been paired
        atRow: The row location of the card
        atCol: the column location of the card
    """
    word: str
    isFaceUp: bool
    isMatched: bool
    atRow: int
    atCol: int

    def __init__(self, word: str, isFaceUp: bool = False, isMatched: bool = False, 
                 atRow: int = -1, atCol: int = -1) -> None:
        """
        Initializing class attributes
        """
        self.word = word
        self.isFaceUp = isFaceUp  
        self.isMatched = isMatched  
        self.atRow = atRow
        self.atCol = atCol

    def __str__(self):
        """
        Returns the word stored on the card
        """
        return self.word