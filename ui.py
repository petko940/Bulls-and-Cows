import tkinter as tk


def start_game():
    start_button.pack_forget()
    Game(root).show()


class Game:
    def __init__(self, root):
        self.clicked_number = tk.StringVar(value='')
        self.clicked_number.set("????")
        self.number_label = tk.Label(
            root,
            textvariable=self.clicked_number,
            font=('Arial', 25),
            width=7,
        )
        self.buttons_numbers_first_row = {}
        self.buttons_numbers_second_row = {}

        for i in range(1, 6):
            self.buttons_numbers_first_row[f"button{i}"] = tk.Button(
                root,
                height=2,
                width=5,
                text=str(i),
                background='lightgreen',
                font=('Arial', 12),
                command=lambda i=i: self.on_number_button_click(str(i), self.buttons_numbers_first_row[f"button{i}"])
            )

        for i in range(6, 10):
            self.buttons_numbers_second_row[f"button{i}"] = tk.Button(
                root,
                height=2,
                width=5,
                text=str(i),
                background='lightgreen',
                font=('Arial', 12),
                command=lambda i=i: self.on_number_button_click(str(i), self.buttons_numbers_second_row[f"button{i}"])
            )

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
        current_number = self.clicked_number.get()
        print(current_number)

    def on_delete_button_click(self):
        self.clicked_number.set('????')
        self.button_enter.config(state='disabled', background='gray')
        for x in self.buttons_numbers_first_row.values():
            x.config(state='normal', background='lightgreen')
        for x in self.buttons_numbers_second_row.values():
            x.config(state='normal', background='lightgreen')

    def show(self):
        self.number_label.place(x=170, y=20)
        for i, button in enumerate(self.buttons_numbers_first_row.values()):
            button.place(x=80 + i * 60, y=80)
        for i, button in enumerate(self.buttons_numbers_second_row.values()):
            button.place(x=80 + i * 60, y=140)

        self.button_enter.place(x=80 + 240, y=140)
        self.button_delete.place(x=390, y=120)

        header_label = tk.Label(root, text="#", width=5, borderwidth=1, relief="solid", font=('Arial', 12))
        header_label.place(x=50, y=220)
        header_label = tk.Label(root, text="Guess", width=20, borderwidth=1, relief="solid", font=('Arial', 12))
        header_label.place(x=95, y=220)
        header_label = tk.Label(root, text="Result", width=20, borderwidth=1, relief="solid", font=('Arial', 12))
        header_label.place(x=275, y=220)


root = tk.Tk()
root.title("Bulls and Cows")

root.geometry("500x600")
root.resizable(False, False)

start_button = tk.Button(
    root,
    text="Start",
    width=20,
    height=5,
    command=start_game
)
start_button.pack(pady=150)

root.mainloop()
