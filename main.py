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
                    if 999 <= current_number <= 9999 and len(set(str(current_number))) == 4:
                        break
                    else:
                        current_number = input("Enter a valid number (digits must be different): ")
                except ValueError:
                    current_number = input("Enter a valid number (digits must be different): ")

            self.moves += 1

            if current_number == random_number:
                self.game_over = True
                print(f"You won in {self.moves} moves!")
                break

            bulls, cows = 0, 0
            for index, num in enumerate(str(current_number)):
                if num == str(random_number)[index]:
                    bulls += 1
                if num in str(random_number) and num != str(random_number)[index]:
                    cows += 1

            print(f"Bulls: {bulls}, Cows: {cows}")


game = Game()
game.play()
