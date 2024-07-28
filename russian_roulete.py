import random
import time

def russian_roulette():
    print("Welcome to Russian Roulette!")
    print("There is a revolver with one bullet in a six-chamber cylinder.")
    print("Players take turns to pull the trigger. Good luck!\n")

    players = int(input("Enter the number of players: "))
    if players < 1:
        print("There must be at least one player.")
        return

    # Initialize the chamber with one bullet
    chamber = [False] * 6
    bullet_position = random.randint(0, 5)
    chamber[bullet_position] = True

    player = 1
    while True:
        print(f"\nPlayer {player}'s turn.")
        input("Press Enter to pull the trigger...")
        time.sleep(1)

        # Spin the cylinder before each pull
        if chamber[random.randint(0, 5)]:
            print("BANG! Player {player} is out!")
            break
        else:
            print("Click... You're safe.")

        # Move to the next player
        player = (player % players) + 1

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    russian_roulette()
