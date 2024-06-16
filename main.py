import tkinter as tk

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monopoly")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)



if __name__ == "__main__":
    game = Game()
    game.root.mainloop()