import random

class CrapsGame:
    def __init__(self):
        self.goal = None

    def roll_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"Rolled: {die1} + {die2} = {total}")
        return total

    def play(self):
        print("=== Welcome to the Dice Game (OOP Version) ===")
        print("--- Initial Roll ---")
        
        first_roll = self.roll_dice()

        if first_roll in (7, 11):
            print(f"Result: You rolled a {first_roll}. You win!")
        elif first_roll in (2, 3, 12):
            print(f"Result: You rolled a {first_roll} (Craps). The casino wins!")
        else:
            self.goal = first_roll
            print(f"Your goal number is set to: {self.goal}. Keep rolling...")
            
            while True:
                current_roll = self.roll_dice()
                
                if current_roll == self.goal:
                    print(f"Result: You hit your goal of {self.goal} again! You win!")
                    break
                elif current_roll == 7:
                    print("Result: You rolled a 7 before hitting your goal. The casino wins!")
                    break

if __name__ == "__main__":
    game = CrapsGame()
    game.play()
