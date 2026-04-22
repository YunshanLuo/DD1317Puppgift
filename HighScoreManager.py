import sqlite3
from typing import List
from pathlib import Path
import pickle

class HighScoreManager:
    """
    Store persistant scores using SQLite
    """

    def __init__(self, dbPath: str = "Highscores.pkl",):
        self.dbPath = dbPath
        self.data = {"easy:": [], "medium": [], "hard": []}

    def saveScore(self):
        with open(self.dbPath, "wb") as f:
            pickle.dump(self.data, f)
    
    def loadScore(self):
        with open(self.dbPath, "rb") as f:
            self.data = pickle.load(f)

    def addScore(self, mode, score):
        self.loadScore()
        self.data[mode].append(score)
        self.data[mode].sort()
        self.saveScore()
    
    def getRank(self, mode, score):
        self.load()
        return self.data[mode].index(score) + 1




    
