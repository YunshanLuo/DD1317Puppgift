import tkinter as tk
import argparse
from Gui import MemoryGameGUI


def main():
    parser = argparse.ArgumentParser(description="Launch Memory Game GUI")
    parser.add_argument("--rows", type=int, default=4, help="Number of rows (even total required)")
    parser.add_argument("--cols", type=int, default=4, help="Number of columns (even total required)")
    args = parser.parse_args()

    total = args.rows * args.cols
    if total % 2 != 0:
        raise SystemExit("Rows * Cols must be even (pairs needed)")

    root = tk.Tk()
    root.title("Memory Game")
    app = MemoryGameGUI(root, rows=args.rows, cols=args.cols)
    root.mainloop()


if __name__ == '__main__':
    main()
