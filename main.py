import itertools
import random
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

        self.dice_1_img = tk.PhotoImage(file="assets/dice_1.png")
        self.dice_2_img = tk.PhotoImage(file="assets/dice_2.png")
        self.dice_3_img = tk.PhotoImage(file="assets/dice_3.png")
        self.dice_4_img = tk.PhotoImage(file="assets/dice_4.png")
        self.dice_5_img = tk.PhotoImage(file="assets/dice_5.png")
        self.dice_6_img = tk.PhotoImage(file="assets/dice_6.png")

        self.show_main_screen()

    def show_main_screen(self):
        self.main_canvas = tk.Canvas(self.root, borderwidth=0)

        self.main_canvas.pack(fill="both", expand=True)

        self.main_canvas.create_image(0, 0, image=self.background_image, anchor="nw")

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
                index += 1

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
        self.player_1_money = tk.Label(
            self.game_screen,
            text="$1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_1_money.place(x=820, y=170, anchor="nw")
        self.player_1_nickname = tk.Label(
            self.game_screen,
            text=self.player_1["name"],
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_1_nickname.place(x=790, y=40, anchor="nw")

        self.player_2_avatar = tk.Label(
            self.game_screen, image=self.player_2_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_2_avatar.place(x=1050, y=50, anchor="nw")
        self.player_2_money = tk.Label(
            self.game_screen,
            text="$1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_2_money.place(x=1070, y=170, anchor="nw")
        self.player_2_nickname = tk.Label(
            self.game_screen,
            text=self.player_2["name"],
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_2_nickname.place(x=1050, y=40, anchor="nw")

        self.player_3_avatar = tk.Label(
            self.game_screen, image=self.player_3_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_3_avatar.place(x=790, y=270, anchor="nw")
        self.player_3_money = tk.Label(
            self.game_screen,
            text="$1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_3_money.place(x=820, y=400, anchor="nw")
        self.player_3_nickname = tk.Label(
            self.game_screen,
            text=self.player_3["name"],
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_3_nickname.place(x=790, y=250, anchor="nw")

        self.player_4_avatar = tk.Label(
            self.game_screen, image=self.player_4_image, borderwidth=0, bg=self.BG_COLOR
        )
        self.player_4_avatar.place(x=1050, y=270, anchor="nw")
        self.player_4_money = tk.Label(
            self.game_screen,
            text="$1500",
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_4_money.place(x=1070, y=400, anchor="nw")
        self.player_4_nickname = tk.Label(
            self.game_screen,
            text=self.player_4["name"],
            borderwidth=0,
            bg=self.BG_COLOR,
            fg="white",
            font=("Arial", 20),
        )
        self.player_4_nickname.place(x=1050, y=250, anchor="nw")

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
        self.determine_order(self.player_1)

        self.root.mainloop()

    def determine_order(self, player):
        self.player_label = tk.Label(
            self.game_screen,
            text=f"{player['name']} will go first",
            borderwidth=0,
            bg="#CCE4D6",
            fg="black",
            font=("Arial", 20),
        )
        self.player_label.place(x=360, y=230, anchor="s")
        self.player_icon = tk.Label(
            self.game_screen,
            image=player["token_display_image"],
            borderwidth=0,
            bg="#CCE4D6",
        )
        self.player_icon.place(x=360, y=255, anchor="n")
        self.root.after(250, lambda: self.roll_dice_for_order(player))

    def roll_dice_for_order(self, player):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        player["high_roll"] = dice_1 + dice_2
        print(dice_1 + dice_2)
        self.display_roll(dice_1, dice_2)
        next_player = next(self.play_order_list)

        if not next_player.get("high_roll"):
            self.root.after(
                1500,
                lambda: (
                    self.player_label.destroy(),
                    self.player_icon.destroy(),
                    self.dice_1.destroy(),
                    self.dice_2.destroy(),
                    self.determine_order(next_player),
                ),
            )
        else:
            self.root.after(
                1500,
                lambda: (
                    self.player_label.destroy(),
                    self.player_icon.destroy(),
                    self.dice_1.destroy(),
                    self.dice_2.destroy(),
                    self.determine_winner(),
                ),
            )

    def display_roll(self, dice1, dice2):
        images = {
            1: self.dice_1_img,
            2: self.dice_2_img,
            3: self.dice_3_img,
            4: self.dice_4_img,
            5: self.dice_5_img,
            6: self.dice_6_img,
        }
        self.dice_1 = tk.Label(
            self.game_screen, image=images[dice1], borderwidth=0, bg=self.BG_COLOR
        )

        self.dice_1.place(x=360, y=560, anchor="e")
        self.dice_2 = tk.Label(
            self.game_screen, image=images[dice2], borderwidth=0, bg=self.BG_COLOR
        )
        self.dice_2.place(x=380, y=560, anchor="w")

    def determine_winner(self):
        highest_score = sorted(
            [self.player_1, self.player_2, self.player_3, self.player_4],
            key=lambda x: x["high_roll"],
        )[-1]
        print(highest_score)

        order_stack = []
        player_list = [self.player_1, self.player_2, self.player_3, self.player_4]
        for player in [self.player_1, self.player_2, self.player_3, self.player_4]:
            player_list.pop()
            if player == highest_score:
                order = [player, *player_list[::-1], *order_stack]
                self.player_order_loop = itertools.cycle(order)
            else:
                order_stack.append(player)

        winner = tk.Label(
            self.game_screen,
            text=f"{highest_score['name']} will go first",
            borderwidth=0,
            bg="#CCE4D6",
            fg="black",
            font=("Arial", 20),
        )
        winner.place(x=360, y=230, anchor="s")

        self.player_1.pop("high_roll")
        self.player_2.pop("high_roll")
        self.player_3.pop("high_roll")
        self.player_4.pop("high_roll")

        self.root.after(
            1750,
            lambda: (
                winner.destroy(),
                self.order_info.destroy(),
                self.start_turn(next(self.player_order_loop)),
            ),
        )

    def start_turn(self, player):
        self.current_player = player
        self.current_player["turn"] = True

        current_player_label = tk.Label(
            self.game_screen,
            text=f"{player['name']}'s turn",
            borderwidth=0,
            bg="#CCE4D6",
            fg="black",
            font=("Arial", 20),
        )
        current_player_label.place(width=500, height=50, x=1000, y=470, anchor="center")

        if player["type"] == "player":
            self.roll_button = tk.Button(
                self.game_screen,
                text="Roll",
                bg="green",
                fg="white",
                font=("Arial", 20),
                command=lambda: (
                    self.confirm_end_turn_show(),
                    self.roll_dice(),
                    self.roll_button.destroy(),
                ),
            )
            self.roll_button.place(width=100, height=50, x=1000, y=550, anchor="center")
        else:
            self.root.after(1000, lambda: self.roll_dice())

    def confirm_end_turn_show(self):
        self.end_turn = tk.Button(
            self.game_screen,
            text="End turn",
            bg="red",
            fg="white",
            borderwidth=0,
            font=("Arial", 20),
            command=lambda: (self.confirm_end_turn_run(), self.end_turn.destroy()),
        )
        self.end_turn.place(width=150, height=60, x=1000, y=600, anchor="nw")

    def confirm_end_turn_run(self):
        self.current_player["turn"] = False
        next_player = next(self.player_order_loop)

        attributes_to_destroy = [
            "current_player_landing",
            "dice_1_display",
            "dice_2_display",
            "property_choice_display",
            "display_label",
            "display_round_bonus",
            "purchase_label",
        ]

        for attribute in attributes_to_destroy:
            if hasattr(self, attribute):
                getattr(self, attribute).destroy()

        self.start_turn(next_player)

    def roll_dice(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        self.total_roll = dice_1 + dice_2

        self.display_roll(dice_1, dice_2)

        if self.current_player["location"] + self.total_roll > 40:
            diff = 40 - (self.current_player["location"] + self.total_roll)
            self.current_player["location"] = -diff
            self.display_round_bonus = tk.Label(
                self.game_screen,
                text="You passed go, collect $200",
                borderwidth=0,
                bg="#CCE4D6",
                fg="black",
                font=("Arial", 20),
            )
            self.display_round_bonus.place(x=360, y=300, anchor="n")
            self.current_player["money"] += 200
            self.update_money()
        else:
            self.current_player["location"] += self.total_roll

        self.current_player_location_property = self.properties[
            self.current_player["location"]
        ]

        x, y = self.current_player_location_property["coordinates"]
        self.board.coords(self.current_player["token"], x, y)
        current_player_move = f"{self.current_player['name']} moved {self.total_roll} spaces,\n&\n landed on {self.current_player_location_property['name']}"
        self.current_player_landing = tk.Label(
            self.game_screen,
            text=current_player_move,
            borderwidth=0,
            bg="#CCE4D6",
            fg="black",
            font=("Arial", 20),
        )
        self.current_player_landing.place(x=360, y=145, anchor="n")

        property_color = self.current_player_location_property["color"]
        property_owner = self.current_player_location_property["owner"]

        if property_color not in [
            "Go",
            "Community Chest",
            "Chance",
            "Tax",
            "Jail",
            "Go to Jail",
            "Free Parking",
        ]:
            if property_owner not in [
                self.player_1,
                self.player_2,
                self.player_3,
                self.player_4,
            ]:
                if (
                    self.current_player_location_property["price"]
                    <= self.current_player["money"]
                ):
                    if self.current_player["type"] == "player":
                        self.property_choice_display = tk.Button(
                            self.game_screen,
                            text=f"BUY: ${self.current_player_location_property['price']}",
                            compound="center",
                            bg="blue",
                            activebackground=self.BG_COLOR,
                            fg="white",
                            borderwidth=0,
                            font=("Arial", 20),
                            command=lambda: (
                                self.buy_place(),
                                self.property_choice_display.destroy(),
                            ),
                        )
                        self.property_choice_display.place(
                            width=170, height=62, x=1012, y=515, anchor="nw"
                        )
                    else:
                        if random.randint(0, 4):
                            self.root.after(500, self.buy_place)
            elif property_color == "Utility":
                if self.current_player != property_owner:
                    self.utility_buy()
            else:
                if self.current_player != property_owner:
                    self.pay_another_player()
        elif property_color == "Tax":
            self.tax_field()
        elif property_color in ["Chance", "Community Chest"]:
            self.card_field()
        elif property_color == "Go to Jail":
            self.current_player["location"] = 11
            self.display_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} has gone to Jail",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=260, anchor="n")
            self.board.coords(self.current_player["token"], 63, 660)

            if self.current_player["type"] == "player":
                self.fine_display = tk.Button(
                    self.game_screen,
                    text="FINE: $50",
                    compound="center",
                    bg=self.BG_COLOR,
                    activebackground=self.BG_COLOR,
                    fg="white",
                    borderwidth=0,
                    font=("Arial", 20),
                    command=lambda: (
                        self.jail_field(),
                        self.fine_display.destroy(),
                    ),
                )
                self.fine_display.place(
                    width=170, height=62, x=1012, y=515, anchor="nw"
                )
                self.end_turn.destroy()
            else:
                self.root.after(500, self.jail_field)

        if self.current_player["type"] == "bot":
            self.root.after(1500, self.confirm_end_turn_run)

    # util methods
    def update_money(self):
        self.player_1_money.config(text=f"${self.player_1['money']}")
        self.player_2_money.config(text=f"${self.player_2['money']}")
        self.player_3_money.config(text=f"${self.player_3['money']}")
        self.player_4_money.config(text=f"${self.player_4['money']}")

    def buy_place(self):
        self.current_player["money"] -= self.current_player_location_property["price"]
        if not self.check_if_game_over():
            self.current_player["properties"].append(self.current_player["location"])
            self.current_player_location_property["owner"] = self.current_player

            self.purchase_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} bought {self.current_player_location_property['name']}",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )

            self.purchase_label.place(x=360, y=380, anchor="n")

            set_color = self.current_player_location_property["color"]
            set_num = 0
            rent = 0

            for t in self.current_player["properties"]:
                if self.properties[t]["color"] == set_color:
                    set_num += 1
                if set_color == "Station":
                    if set_num == 1:
                        rent = 75
                    elif set_num == 2:
                        rent = 100
                    elif set_num == 3:
                        rent = 125
                    elif set_num == 4:
                        rent = 150
                else:
                    if set_num == 1:
                        rent = self.current_player_location_property["price"] // 2
                    elif set_num == 2:
                        rent = self.current_player_location_property["price"]
                    elif set_num == 3:
                        rent = self.current_player_location_property["price"] * 2

            for t in self.current_player["properties"]:
                if self.properties[t]["color"] == set_color:
                    self.properties[t]["rent"] = rent

    def check_if_game_over(self):
        if self.current_player["money"] < 0:
            self.display_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} is bankrupt",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=280, anchor="n")

            self.root.after(2000, self.game_over)
            return True
        else:
            self.update_money()
            return False

    def utility_buy(self):
        count = 0
        for t in self.current_player_location_property["owner"]["properties"]:
            if self.properties[t]["color"] == "Utility":
                count += 1

        if count == 1:
            self.current_player["money"] -= self.total_roll * 4
            if not self.check_if_game_over():
                self.current_player_location_property["owner"]["money"] += (
                    self.total_roll * 4
                )
                self.update_money()
                self.display_label = tk.Label(
                    self.game_screen,
                    text=f"{self.current_player['name']} paid {self.total_roll * 4} to {self.current_player_location_property['owner']['name']}",
                    borderwidth=0,
                    bg=self.BG_COLOR,
                    fg="white",
                    font=("Arial", 20),
                )
                self.display_label.place(x=360, y=380, anchor="n")
        elif count == 2:
            self.current_player["money"] -= self.total_roll * 10
            if not self.check_if_game_over():
                self.current_player_location_property["owner"]["money"] += (
                    self.total_roll * 10
                )
                self.update_money()
                self.display_label = tk.Label(
                    self.game_screen,
                    text=f"{self.current_player['name']} paid {self.total_roll * 10} to {self.current_player_location_property['owner']['name']}",
                    borderwidth=0,
                    bg=self.BG_COLOR,
                    fg="white",
                    font=("Arial", 20),
                )
                self.display_label.place(x=360, y=280, anchor="n")

    def tax_field(self):
        self.current_player["money"] -= self.current_player_location_property["price"]
        if not self.check_if_game_over():
            self.display_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} paid {self.current_player_location_property['price']} tax",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=280, anchor="n")

    def card_field(self):

        result = ""

        if self.current_player_location_property["name"] == "Chance":
            get_card = self.chances.pop(0)
            self.chances.append(get_card)

            if get_card["action"] == "give":
                self.current_player["money"] -= get_card["value"]
                result = f"Chance \n\n {get_card['name']} \n\n {self.current_player['name']} paid {get_card['value']}"
            elif get_card["action"] == "get":
                self.current_player["money"] += get_card["value"]
                result = f"Chance \n\n {get_card['name']} \n\n {self.current_player['name']} received {get_card['value']}"
            elif get_card["action"] == "giveall":
                self.current_player["money"] -= get_card["value"]
                for player in [
                    self.player_1,
                    self.player_2,
                    self.player_3,
                    self.player_4,
                ]:
                    if player != self.current_player:
                        player["money"] += 50
                result = f"Chance \n\n {get_card['name']} \n\n {self.current_player['name']} paid {get_card['value']} to all players"
            elif get_card["action"] == "move":
                self.current_player["location"] = 1
                self.current_player["money"] += 200
                result = f"Chance \n\n {get_card['name']} \n\n {self.current_player['name']} moved to go field"
                self.board.coords(self.current_player["token"], 675, 675)
        else:
            get_card = self.chests.pop(0)
            self.chests.append(get_card)
            if get_card["action"] == "give":
                self.current_player["money"] -= get_card["value"]
                result = f"Community Chest \n\n {get_card['name']} \n\n {self.current_player['name']} paid {get_card['value']}"
            elif get_card["action"] == "get":
                self.current_player["money"] += get_card["value"]
                result = f"Community Chest \n\n {get_card['name']} \n\n {self.current_player['name']} received {get_card['value']}"
            elif get_card["action"] == "move":
                self.current_player["location"] = 1
                self.current_player["money"] += 200
                result = f"Community Chest \n\n {get_card['name']} \n\n {self.current_player['name']} moved to go field"
                self.board.coords(self.current_player["token"], 675, 675)

        if not self.check_if_game_over():
            self.display_label = tk.Label(
                self.game_screen,
                text=result,
                borderwidth=0,
                bg="#CCE4D6",
                fg="black",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=280, anchor="n")

    def jail_field(self):
        self.current_player["money"] -= 50
        if not self.check_if_game_over():
            self.display_label.destroy()
            self.display_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} paid $50 to get out of jail",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=280, anchor="n")

            if self.current_player["type"] == "player":
                self.confirm_end_turn_show()

    def pay_another_player(self):
        self.current_player["money"] -= self.current_player_location_property["rent"]
        if not self.check_if_game_over():
            self.current_player_location_property["owner"][
                "money"
            ] += self.current_player_location_property["rent"]
            self.update_money()
            self.display_label = tk.Label(
                self.game_screen,
                text=f"{self.current_player['name']} paid {self.current_player_location_property['rent']} to {self.current_player_location_property['owner']['name']}",
                borderwidth=0,
                bg=self.BG_COLOR,
                fg="white",
                font=("Arial", 20),
            )
            self.display_label.place(x=360, y=280, anchor="n")


if __name__ == "__main__":
    Game()
