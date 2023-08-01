import tkinter as tk
from random import shuffle


class Game:
    def __init__(self, root):
        self.root = root
        self.random_number = self.generate_random_number()
        self.clicked_number = tk.StringVar(value='')
        self.clicked_number.set("????")
        self.number_label = tk.Label(
            root,
            textvariable=self.clicked_number,
            font=('Arial', 25),
            width=7,
        )
        self.buttons_numbers_first_row = None
        self.buttons_numbers_second_row = None
        self.create_buttons()

        self.button_delete = tk.Button(
            root,
            text="delete",
            command=self.on_delete_button_click,
            font=('Arial', 16),
            width=5,
        )
        self.button_enter = tk.Button(
            root,
            text="\u21B2",
            command=self.on_button_enter,
            font=('Arial', 19),
            width=3,
            state='disabled',
            background='gray'
        )
        self.bulls = None
        self.cows = None
        self.data = []
        self.is_winning = False
        self.game_ended = False
        self.moves = 0

    def create_buttons(self):
        self.buttons_numbers_first_row = {}
        for i in range(1, 6):
            self.buttons_numbers_first_row[f"button{i}"] = tk.Button(
                self.root,
                height=2,
                width=5,
                text=str(i),
                background='lightgreen',
                font=('Arial', 12),
                command=lambda i=i: self.on_number_button_click(str(i), self.buttons_numbers_first_row[f"button{i}"])
            )

        self.buttons_numbers_second_row = {}
        for i in range(6, 10):
            self.buttons_numbers_second_row[f"button{i}"] = tk.Button(
                self.root,
                height=2,
                width=5,
                text=str(i),
                background='lightgreen',
                font=('Arial', 12),
                command=lambda i=i: self.on_number_button_click(str(i), self.buttons_numbers_second_row[f"button{i}"])
            )

    @staticmethod
    def generate_random_number():
        digits = list(range(1, 10))
        shuffle(digits)
        digits = digits[:4]
        return int(''.join(map(str, digits)))

    def on_number_button_click(self, number, button):
        if len(self.clicked_number.get()) == 4 and self.clicked_number.get() != "????":
            return

        if self.clicked_number.get().startswith("????"):
            self.clicked_number.set(number)
        else:
            self.clicked_number.set(self.clicked_number.get() + number)

        button.config(state='disabled', background='gray')

        if len(self.clicked_number.get()) == 4 and self.clicked_number.get() != "????":
            self.button_enter.config(state='normal', background='white')
            return

    def on_button_enter(self):
        self.moves += 1
        current_number = self.clicked_number.get()
        if current_number == '????':
            return None, None

        current_number = int(current_number)

        bulls, cows = 0, 0
        for index, num in enumerate(str(current_number)):
            if num == str(self.random_number)[index]:
                bulls += 1
            if num in str(self.random_number) and num != str(self.random_number)[index]:
                cows += 1

        if bulls == 4:
            self.is_winning = True
            self.end_game()

        self.bulls = bulls
        self.cows = cows

        self.data.append((current_number, bulls, cows))
        if len(self.data) == 10:
            self.end_game()

        self.result()
        self.on_delete_button_click()

    def result(self):
        if not self.game_ended:
            print(self.data)

            header = tk.Label(self.root, text="#", width=5, borderwidth=1, relief="solid", font=('Arial', 12))
            header.place(x=50, y=220)
            header = tk.Label(self.root, text="Guess", width=20, borderwidth=1, relief="solid", font=('Arial', 12))
            header.place(x=95, y=220)
            header = tk.Label(self.root, text="Result", width=20, borderwidth=1, relief="solid", font=('Arial', 12))
            header.place(x=275, y=220)

            y = 245
            for x in range(len(self.data)):
                num = tk.Label(
                    self.root,
                    text=x + 1,
                    font=('Arial', 12)
                )
                num.place(x=67, y=y)

                guess = tk.Label(
                    self.root,
                    text=f"{self.data[x][0]}",
                    font=('Arial', 12)
                )
                guess.place(x=170, y=y)
                result = tk.Label(
                    self.root,
                    text=f"{self.data[x][1]} Bulls | {self.data[x][2]} Cows",
                    font=('Arial', 12)
                )
                result.place(x=310, y=y)
                y += 30

    def on_delete_button_click(self):
        self.clicked_number.set('????')
        try:
            self.button_enter.config(state='disabled', background='gray')
            for x in self.buttons_numbers_first_row.values():
                x.config(state='normal', background='lightgreen')
            for x in self.buttons_numbers_second_row.values():
                x.config(state='normal', background='lightgreen')
        except:
            pass

    def show(self):
        self.number_label.place(x=170, y=20)
        for i, button in enumerate(self.buttons_numbers_first_row.values()):
            button.place(x=80 + i * 60, y=80)
        for i, button in enumerate(self.buttons_numbers_second_row.values()):
            button.place(x=80 + i * 60, y=140)

        self.button_enter.place(x=80 + 240, y=140)
        self.button_delete.place(x=390, y=120)
        self.root.mainloop()

    def end_game(self):
        self.game_ended = True
        self.root.destroy()
        root1 = tk.Tk()
        root1.title("End")
        root1.geometry("300x300")
        root1.resizable(False, False)

        def play_again():
            root1.destroy()
            root = tk.Tk()
            root.title("Bulls and Cows")

            root.geometry("500x700")
            root.resizable(False, False)

            new_game = Game(root)
            new_game.show()

            root.mainloop()

        def exit_game():
            exit()

        if self.is_winning:
            win_message = tk.Label(
                root1,
                text=f"You won in {self.moves} moves",
                font=('Arial', 16),
                width=30,
            )
            win_message.pack(pady=30)
        else:
            lose_message = tk.Label(
                root1,
                text="You lose",
                font=('Arial', 16),
                width=10,
            )
            lose_message.pack(pady=30)

        wining_number = tk.Label(
            root1,
            text=f"Winning numbers is: {self.random_number}",
            font=('Arial', 16),
            width=100,
        )
        wining_number.pack()

        play_button = tk.Button(
            root1,
            text="Play again",
            font=('Arial', 16),
            background="lightgreen",
            command=play_again
        )
        play_button.place(x=50, y=170)

        exit_button = tk.Button(
            root1,
            text="Exit",
            font=('Arial', 16),
            background="red",
            command=exit_game
        )
        exit_button.place(x=190, y=170)

        root1.mainloop()


def start_game():
    start_button.pack_forget()
    game.show()


root = tk.Tk()
root.title("Bulls and Cows")

root.geometry("500x600")
root.resizable(False, False)

game = Game(root)
start_button = tk.Button(
    root,
    text="Start",
    width=20,
    height=5,
    command=start_game
)
start_button.pack(pady=150)

root.mainloop()
