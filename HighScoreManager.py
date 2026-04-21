from typing import List
from pathlib import Path

class HighScoreManager:
    """
    Attributes:
        currScore (int): The current score
        scores (List): list of all previous scores read from the file
        filePath: The location which the Highscores.txt file exists    
    """
    currScore: int 
    scores: List[int]
    filePath: str

    def __init__(self,currScore:int, scores: List[int] = [], 
                 filePath: str= "/Highscores.txt"):
        """
        Initiates all attributes
        """
        self.currScore = currScore
        self.scores = scores 
        self.filePath = filePath
    
    def loadScores(self):
        """
        Loads the previous highscores from the file in file path
        """
        with open(self.filePath) as f:
            self.scores = [int(line.strip()) for line in f]
    
    def writeScore(self):
        """
        Write the current high score in descending order into the txt file
        """
        sortedScores = sorted(self.scores)
        with open(self.filePath, "w") as f:
            for score in sortedScores:
                f.write(f"{score}\n")
    
    def currRank(self):
        """
        Gets current rank compared to previous high scores
        """
        allScores = self.scores.append(self.currScore)
        rank = sorted(allScores).index(self.currScore)
        return rank



    


    
