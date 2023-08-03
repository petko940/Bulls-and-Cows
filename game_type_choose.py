from console import ConsoleGame

if __name__ == '__main__':
    while True:
        print("""------------------------------
    Enter number
    1 - Console game
    2 - GUI Game
    3 - Exit
------------------------------""")
        choice = int(input())
        if choice == 1:
            while True:
                console = ConsoleGame()
                console.play()
                if not console.play_again():
                    break

        elif choice == 2:
            import tkinter as tk
            from ui import Game


            def start_game():
                start_button.pack_forget()
                game.show()


            root = tk.Tk()
            root.title("Bulls and Cows")

            root.geometry("500x600+600+100")
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
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid number. Please choose again.")
