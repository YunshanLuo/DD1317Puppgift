from typing import List

class HighScoreManager:
    def __init__(self, highscores: List[int] = None, attempt: int = 0) -> None:
        self.highscore = highscores if highscores is not None else []
        self.attempt = attempt

    def getRank(self) -> int:
        allScores = self.highscore + [self.attempt]
        sortedAllScores = sorted(allScores)
        return sortedAllScores.index(self.attempt) + 1

    def parseFile(self, fileName: str = "Highscores.txt") -> None:
        self.highscore = []
        try:
            with open(fileName) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            self.highscore.append(int(line))
                        except ValueError:
                            continue
        except FileNotFoundError:
            self.highscore = []

    def saveScore(self, fileName: str = "Highscores.txt") -> None:
        try:
            with open(fileName, 'w') as f:
                for score in self.highscore:
                    f.write(f"{score}\n")
        except Exception:
            pass
    


    
