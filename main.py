from random import shuffle


class Game:
    def __init__(self):
        self.game_over = False
        self.moves = 0

    @staticmethod
    def generate_random_number():
        digits = list(range(1, 10))
        shuffle(digits)
        digits = digits[:4]
        return int(''.join(map(str, digits)))

    def play(self):
        random_number = self.generate_random_number()
        while not self.game_over:
            current_number = input("Enter a four-digit number (digits must be different): ")
            while True:
                try:
                    current_number = int(current_number)
                    if 999 <= current_number <= 9999:
                        break
                    else:
                        current_number = input("Enter a valid number (digits must be different): ")
                except ValueError:
                    current_number = input("Enter a valid number (digits must be different): ")

            if current_number == random_number:
                self.moves += 1
                self.game_over = True
                print(f"You won in {self.moves} moves!")


game = Game()
game.play()
