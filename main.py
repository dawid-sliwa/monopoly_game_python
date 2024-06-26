import itertools
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

        self.board_image = tk.PhotoImage(file="assets/board.png")

        self.player_1 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "player",
        }

        self.player_2 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "bot",
        }

        self.player_3 = {
            "location": 1,
            "money": 1500,
            "properties": [],
            "turn": False,
            "type": "bot",
        }

        self.player_4 = {
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
            command=self.begin_game,
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
        try:
            self.player_1["name"] = (
                self.player_1_entry.get()
                if self.player_1_entry.get() != ""
                else "Player 1"
            )
            self.player_2["name"] = (
                self.player_2_entry.get()
                if self.player_2_entry.get() != ""
                else "Player 2"
            )
            self.player_3["name"] = (
                self.player_3_entry.get()
                if self.player_3_entry.get() != ""
                else "Player 3"
            )
            self.player_4["name"] = (
                self.player_4_entry.get()
                if self.player_4_entry.get() != ""
                else "Player 4"
            )
            self.player_select.destroy()
        except Exception as e:
            print(e)

        for player in (
            self.player_1,
            self.player_2,
            self.player_3,
            self.player_4,
        ):
            player["location"] = 1
            player["money"] = 1500
            player["properties"] = []
            player["turn"] = False

        self.player_1["token_display_image"] = self.player_1_image
        self.player_1["avatar_image"] = tk.PhotoImage(file="assets/shoe_avatar.png")
        self.player_2["token_display_image"] = self.player_2_image
        self.player_2["avatar_image"] = tk.PhotoImage(file="assets/car_avatar.png")
        self.player_3["token_display_image"] = self.player_3_image
        self.player_3["avatar_image"] = tk.PhotoImage(file="assets/hat_avatar.png")
        self.player_4["token_display_image"] = self.player_4_image
        self.player_4["avatar_image"] = tk.PhotoImage(file="assets/dog_avatar.png")

        self.game_screen = tk.Frame(self.root, bg=self.BG_COLOR)
        self.game_screen.pack(fill="both", expand=True)

        self.board = tk.Canvas(self.game_screen, borderwidth=0)
        self.board.place(width=720, height=720, anchor="nw")
        self.board.create_image(0, 0, image=self.board_image, anchor="nw")
        # self.board.bind()

        self.chances = []
        self.chests = []

        with open("cards.json") as f:
            data = json.load(f)
            for card in data:
                card_obj = {}
                card_obj["group"] = card["type"]
                card_obj["action"] = card["action"]
                card_obj["value"] = card["val"]
                card_obj["name"] = card["description"]
                if card_obj["group"] == "c":
                    self.chances.append(card_obj)
                else:
                    self.chests.append(card_obj)

        self.properties = {}

        with open("properties.json") as f:
            data = json.load(f)
            index = 1
            for prop in data:
                property_obj = {"owner": None}

                self.properties[index] = property_obj

                property_obj["name"] = prop["name"]
                property_obj["price"] = prop["price"]
                property_obj["color"] = prop["color"]
                property_obj["coordinates"] = eval(prop["coordinates"])

        self.card_properties = {}

        with open("propertycards.json") as f:
            data = json.load(f)
            for card in data:
                card_obj = {}
                self.card_properties[eval(card["coordinates"])] = card
                card_obj["id"] = card["id"]
                card_obj["color"] = card["color"]

        self.player_1_avatar = tk.Label(
            self.game_screen, image=self.player_1_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_1_avatar.place(x=790, y=50, anchor="nw")
        self.p1_money_avatar = tk.Label(
            self.game_screen,
            image=self.player_1["avatar_image"],
            borderwidth=0,
            bg=self.BG_COLOR,
        )
        self.p1_money_avatar.place(x=750, y=500, anchor="nw")
        self.player_1_money = tk.Label(
            self.game_screen,
            text=": $1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_1_money.place(x=790, y=500, anchor="nw")

        self.player_2_avatar = tk.Label(
            self.game_screen, image=self.player_2_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_2_avatar.place(x=1050, y=50, anchor="nw")
        self.p2_money_avatar = tk.Label(
            self.game_screen,
            image=self.player_2["avatar_image"],
            borderwidth=0,
            bg=self.BG_COLOR,
        )
        self.p2_money_avatar.place(x=750, y=550, anchor="nw")
        self.player_2_money = tk.Label(
            self.game_screen,
            text=": $1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_2_money.place(x=790, y=550, anchor="nw")

        self.player_3_avatar = tk.Label(
            self.game_screen, image=self.player_3_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_3_avatar.place(x=790, y=270, anchor="nw")
        self.p3_money_avatar = tk.Label(
            self.game_screen,
            image=self.player_3["avatar_image"],
            borderwidth=0,
            bg=self.BG_COLOR,
        )
        self.p3_money_avatar.place(x=750, y=600, anchor="nw")
        self.player_3_money = tk.Label(
            self.game_screen,
            text=": $1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_3_money.place(x=790, y=600, anchor="nw")

        self.player_4_avatar = tk.Label(
            self.game_screen, image=self.player_4_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_4_avatar.place(x=1050, y=270, anchor="nw")

        self.p4_money_avatar = tk.Label(
            self.game_screen,
            image=self.player_4["avatar_image"],
            borderwidth=0,
            bg=self.BG_COLOR,
        )
        self.p4_money_avatar.place(x=750, y=650, anchor="nw")
        self.player_4_money = tk.Label(
            self.game_screen,
            text=": $1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_4_money.place(x=790, y=650, anchor="nw")

        self.player_1["token"] = self.board.create_image(
            651, 650, image=self.player_1["avatar_image"], anchor="center"
        )
        self.player_2["token"] = self.board.create_image(
            651, 695, image=self.player_2["avatar_image"], anchor="center"
        )
        self.player_3["token"] = self.board.create_image(
            696, 650, image=self.player_3["avatar_image"], anchor="center"
        )
        self.player_4["token"] = self.board.create_image(
            696, 695, image=self.player_4["avatar_image"], anchor="center"
        )

        self.order_info = tk.Label(
            self.game_screen,
            text="Who will go first?\n",
            borderwidth=0,
            bg="#CCE4D6",
            fg="black",
            font=("Arial", 20),
        )
        self.order_info.place(x=360, y=145, anchor="n")

        self.current_player = {"type": "pc"}
        self.play_order_list = itertools.cycle(
            (self.player_2, self.player_3, self.player_4)
        )
        self.determine_order()

        self.root.mainloop()

    def determine_order(self):
        pass

    def roll_dice_for_order(self):
        pass


if __name__ == "__main__":
    Game()
