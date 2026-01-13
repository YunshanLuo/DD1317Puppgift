import tkinter as tk
from tkinter import messagebox
import random
from Card import Card
from Board import Board
from HighScoreManager import HighScoreManager


class MemoryGameGUI:
    def __init__(self, master, rows: int = 4, cols: int = 4):
        if (rows * cols) % 2 != 0:
            raise ValueError("Board must have an even number of cells")
        self.master = master
        self.rows = rows
        self.cols = cols
        self.attempts = 0
        self.first = None
        self.second = None
        self.buttons = {}

        # generate sample words and pairs
        sample_words = [
            'Cat', 'Dog', 'Apple', 'Ball', 'Tree', 'Car', 'Sun', 'Moon',
            'Star', 'Book', 'Key', 'Cup', 'Pen', 'Bird', 'Fish', 'Hat'
        ]
        needed = (rows * cols) // 2
        words = sample_words[:needed]
        pair_list = words + words
        random.shuffle(pair_list)

        # create Card objects
        cards = []
        idx = 0
        for r in range(rows):
            for c in range(cols):
                word = pair_list[idx]
                idx += 1
                card = Card(word=word, isFaceUp=False, isMatched=False, atRow=r, atCol=c)
                cards.append(card)

        self.board = Board(rows, cols, cards)

        # UI layout
        top_frame = tk.Frame(master)
        top_frame.pack(padx=8, pady=8)

        self.attempts_var = tk.StringVar(value=f"Attempts: {self.attempts}")
        attempts_label = tk.Label(top_frame, textvariable=self.attempts_var)
        attempts_label.pack(side=tk.LEFT, padx=(0, 12))

        restart_btn = tk.Button(top_frame, text="Restart", command=self.restart)
        restart_btn.pack(side=tk.LEFT)

        grid_frame = tk.Frame(master)
        grid_frame.pack(padx=8, pady=8)

        for card in self.board.cards:
            btn = tk.Button(grid_frame, text="", width=12, height=4,
                            command=lambda r=card.atRow, c=card.atCol: self.on_click(r, c))
            btn.grid(row=card.atRow, column=card.atCol, padx=4, pady=4)
            self.buttons[(card.atRow, card.atCol)] = btn

    def on_click(self, row: int, col: int):
        card = self.board.getCard(row, col)
        if card is None or card.isMatched or card.isFaceUp:
            return

        btn = self.buttons[(row, col)]
        btn.config(text=card.getText())
        card.isFaceUp = True

        if self.first is None:
            self.first = card
            return

        if self.second is None:
            self.second = card
            self.attempts += 1
            self.attempts_var.set(f"Attempts: {self.attempts}")
            self.master.after(600, self.check_match)

    def check_match(self):
        if self.first and self.second:
            if self.first.getText() == self.second.getText():
                # mark matched
                self.first.isMatched = True
                self.second.isMatched = True
                b1 = self.buttons[(self.first.atRow, self.first.atCol)]
                b2 = self.buttons[(self.second.atRow, self.second.atCol)]
                b1.config(state=tk.DISABLED)
                b2.config(state=tk.DISABLED)
            else:
                # flip back
                b1 = self.buttons[(self.first.atRow, self.first.atCol)]
                b2 = self.buttons[(self.second.atRow, self.second.atCol)]
                b1.config(text="")
                b2.config(text="")
                self.first.isFaceUp = False
                self.second.isFaceUp = False

        self.first = None
        self.second = None

        if all(card.isMatched for card in self.board.cards):
            self.on_win()

    def on_win(self):
        hsm = HighScoreManager()
        hsm.parseFile()
        hsm.attempt = self.attempts
        hsm.highscore.append(self.attempts)
        hsm.saveScore()
        rank = hsm.getRank()
        messagebox.showinfo("You won!", f"You won in {self.attempts} attempts. Rank: {rank}")

    def restart(self):
        # recreate shuffled board
        total = self.rows * self.cols
        sample_words = [
            'Cat', 'Dog', 'Apple', 'Ball', 'Tree', 'Car', 'Sun', 'Moon',
            'Star', 'Book', 'Key', 'Cup', 'Pen', 'Bird', 'Fish', 'Hat'
        ]
        needed = total // 2
        words = sample_words[:needed]
        pair_list = words + words
        random.shuffle(pair_list)

        idx = 0
        for r in range(self.rows):
            for c in range(self.cols):
                card = self.board.getCard(r, c)
                word = pair_list[idx]
                idx += 1
                card.word = word
                card.isFaceUp = False
                card.isMatched = False
                btn = self.buttons[(r, c)]
                btn.config(text="", state=tk.NORMAL)

        self.attempts = 0
        self.attempts_var.set(f"Attempts: {self.attempts}")
        self.first = None
        self.second = None


def main():
    root = tk.Tk()
    root.title("Memory Game")
    app = MemoryGameGUI(root, rows=4, cols=4)
    root.mainloop()


if __name__ == '__main__':
    main()
