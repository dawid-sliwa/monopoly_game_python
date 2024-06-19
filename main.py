import tkinter as tk


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monopoly")
        self.root.geometry("1260x720")
        self.root.resizable(False, False)

        self.background_image = tk.PhotoImage(file="assets/background.png")
        self.back_image = tk.PhotoImage(file="assets/back.png")

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
            lambda event: (self.main_canvas.destroy(), self.show_menu_screen()),
        )

        self.main_canvas.focus_set()

        self.root.mainloop()

    def show_menu_screen(self):
        self.menu_frame = tk.Frame(self.root, bg="gray")
        self.menu_frame.pack(fill="both", expand=True)

        back_button = tk.Button(
            self.menu_frame,
            borderwidth=0,
            image=self.back_image,
            bg="gray",
            activebackground="gray",
            command=lambda: (self.menu_frame.destroy(), self.show_main_screen()),
        )
        back_button.place(relx=0.01, rely=0.01, anchor="nw")

        self.root.mainloop()


if __name__ == "__main__":
    Game()
