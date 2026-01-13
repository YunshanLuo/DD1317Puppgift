
class Card:
    """
    Card object representing a card in the MemoryGame
    """
    word: str
    isFaceUp: bool
    isMatched: bool
    atRow: int
    atCol: int

    def __init__(self, word: str, isFaceUp: bool = False, isMatched: bool = False, 
                 atRow: int = -1, atCol: int = -1) -> None:
        """
        Initializing class variables
        """
        self.word = word  # Contained word 
        self.isFaceUp = isFaceUp  # Is currently face up
        self.isMatched = isMatched  # Has already been matched
        self.atRow = atRow
        self.atCol = atCol

    def getText(self) -> str:
        """
        Returns the word on the card
        """
        return self.word
    