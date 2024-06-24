import tkinter as tk
import json


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monopoly")
        self.root.geometry("1260x720")
        self.root.resizable(False, False)

        self.background_image = tk.PhotoImage(file="assets/background.png")
        self.back_image = tk.PhotoImage(file="assets/back.png")

        self.shoe_image = tk.PhotoImage(file="assets/shoe.png")

        self.player1 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "player",
        }

        self.player2 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "bot",
        }

        self.player3 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "bot",
        }

        self.player4 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "bot",
        }

        self.BG_COLOR = "#1D1D12"

        self.show_main_screen()

    def show_main_screen(self):
        self.main_canvas = tk.Canvas(self.root, borderwidth=0)

        self.main_canvas.pack(fill="both", expand=True)

        self.main_canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        press_button_label = tk.Label(
            self.main_canvas,
            borderwidth=0,
            text="Press anything to start",
            font=("Arial", 40),
            fg="white",
            compound="center",
        )

        press_button_label.place(relx=0.5, rely=0.5, anchor="center", width=1260)

        self.main_canvas.bind(
            "<KeyPress>",
            lambda event: (self.main_canvas.destroy(), self.player_select_screen()),
        )

        self.main_canvas.focus_set()

        self.root.mainloop()

    def player_select_screen(self):
        self.player_select = tk.Frame(self.root, bg=self.BG_COLOR)
        self.player_select.pack(fill="both", expand=True)

        back_button = tk.Button(
            self.player_select,
            borderwidth=0,
            image=self.back_image,
            bg=self.BG_COLOR,
            activebackground=self.BG_COLOR,
            command=lambda: (self.player_select.destroy(), self.show_main_screen()),
        )
        back_button.place(relx=0.01, rely=0.01, anchor="nw")
        player_select = tk.Label(
            self.player_select,
            borderwidth=0,
            text="Player select",
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        player_select.place(x=532, y=162.5, width=216, height=53, anchor="nw")

        start_game_button = tk.Button(
            self.player_select,
            borderwidth=0,
            text="Start game",
            bg="green",
            fg="white",
            font=("Arial", 20),
            command=lambda: (self.player_select.destroy(), self.game_screen()),
        )
        start_game_button.place(x=532, y=562.5, width=216, height=53, anchor="nw")

        # player 1
        self.player_1_index = 0
        self.player_1_image = tk.PhotoImage(file="assets/shoe.png")

        self.player_1_image_label = tk.Label(
            self.player_select,
            image=self.player_1_image,
            borderwidth=0,
            bg=self.BG_COLOR,
        )
        self.player_1_image_label.place(x=96, y=390, anchor="nw")

        self.player_1_entry = tk.Entry(
            self.player_select,
            borderwidth=0,
            bg="white",
            fg="gray",
            font=("Arial", 20),
            justify="center",
        )
        self.player_1_entry.insert(0, "Player 1")
        self.player_1_entry.place(x=150, y=300, width=144, height=45, anchor="center")
        self.player_1_entry.bind(
            "<FocusIn>",
            lambda event: (
                (
                    self.player_1_entry.delete(0, tk.END),
                    self.player_1_entry.configure(fg="black"),
                )
                if self.player_1_entry.get() == "Player 1"
                else None
            ),
        )
        self.player_1_entry.bind(
            "<FocusOut>",
            lambda event: (
                (
                    self.player_1_entry.insert(0, "Player 1"),
                    self.player_1_entry.configure(fg="grey"),
                )
                if self.player_1_entry.get() == ""
                else None
            ),
        )

        self.player1_type = "player"
        self.player1_type_label = tk.Label(
            self.player_select,
            text="Player",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player1_type_label.place(x=150, y=400, anchor="s")

        # player 2
        self.player_2_index = 1
        self.player_2_image = tk.PhotoImage(file="assets/car.png")
        self.player_2_image_label = tk.Label(
            self.player_select,
            borderwidth=0,
            image=self.player_2_image,
            bg=self.BG_COLOR,
        )
        self.player_2_image_label.place(x=408, y=390, anchor="nw")
        self.player_2_entry = tk.Entry(
            self.player_select,
            borderwidth=0,
            bg="white",
            fg="gray",
            font=("Arial", 20),
            justify="center",
        )
        self.player_2_entry.place(x=468, y=300, width=144, height=45, anchor="center")
        self.player_2_entry.insert(0, "Player 2")
        self.player_2_entry.bind(
            "<FocusIn>",
            lambda event: (
                (
                    self.player_2_entry.delete(0, tk.END),
                    self.player_2_entry.configure(fg="black"),
                )
                if self.player_2_entry.get() == "Player 2"
                else None
            ),
        )
        self.player_2_entry.bind(
            "<FocusOut>",
            lambda event: (
                (
                    self.player_2_entry.insert(0, "Player 2"),
                    self.player_2_entry.configure(fg="grey"),
                )
                if self.player_2_entry.get() == ""
                else None
            ),
        )
        self.player_2_type = "computer"
        self.player_2_type_label = tk.Label(
            self.player_select,
            text="Computer",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_2_type_label.place(x=468, y=400, anchor="s")

        # player 3
        self.player_3_index = 2
        self.player_3_image = tk.PhotoImage(file="assets/hat.png")
        self.player_3_image_label = tk.Label(
            self.player_select,
            borderwidth=0,
            image=self.player_3_image,
            bg=self.BG_COLOR,
        )
        self.player_3_image_label.place(x=726, y=390, anchor="nw")
        self.player_3_entry = tk.Entry(
            self.player_select,
            borderwidth=0,
            bg="white",
            fg="gray",
            font=("Arial", 20),
            justify="center",
        )
        self.player_3_entry.place(x=786, y=300, width=144, height=45, anchor="center")
        self.player_3_entry.insert(0, "Player 3")
        self.player_3_entry.bind(
            "<FocusIn>",
            lambda event: (
                (
                    self.player_3_entry.delete(0, tk.END),
                    self.player_3_entry.configure(fg="black"),
                )
                if self.player_3_entry.get() == "Player 3"
                else None
            ),
        )
        self.player_3_entry.bind(
            "<FocusOut>",
            lambda event: (
                (
                    self.player_3_entry.insert(0, "Player 3"),
                    self.player_3_entry.configure(fg="grey"),
                )
                if self.player_3_entry.get() == ""
                else None
            ),
        )
        self.player_3_type = "computer"
        self.player_3_type_label = tk.Label(
            self.player_select,
            text="Computer",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_3_type_label.place(x=786, y=400, anchor="s")

        # player 4
        self.player_4_index = 3
        self.player_4_image = tk.PhotoImage(file="assets/dog.png")
        self.player_4_image_label = tk.Label(
            self.player_select,
            borderwidth=0,
            image=self.player_4_image,
            bg=self.BG_COLOR,
        )
        self.player_4_image_label.place(x=1044, y=390, anchor="nw")
        self.player_4_entry = tk.Entry(
            self.player_select,
            borderwidth=0,
            bg="white",
            fg="gray",
            font=("Arial", 20),
            justify="center",
        )
        self.player_4_entry.place(x=1104, y=300, width=144, height=45, anchor="center")
        self.player_4_entry.insert(0, "Player 4")
        self.player_4_entry.bind(
            "<FocusIn>",
            lambda event: (
                (
                    self.player_4_entry.delete(0, tk.END),
                    self.player_4_entry.configure(fg="black"),
                )
                if self.player_4_entry.get() == "Player 4"
                else None
            ),
        )
        self.player_4_entry.bind(
            "<FocusOut>",
            lambda event: (
                (
                    self.player_4_entry.insert(0, "Player 4"),
                    self.player_4_entry.configure(fg="grey"),
                )
                if self.player_4_entry.get() == ""
                else None
            ),
        )
        self.player_4_type = "computer"
        self.player_4_type_label = tk.Label(
            self.player_select,
            text="Computer",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_4_type_label.place(x=1104, y=400, anchor="s")

        self.root.mainloop()

    def begin_game(self):
        pass


if __name__ == "__main__":
    Game()
