# Dice Rolling Game
import random

print("=" * 30)
print("🎲 Welcome to Dice Roller 🎲")
print("=" * 30)

# Initialize game statistics
best_roll = 0
roll_counter = 0

# Main game loop
while True:
    choice = input("\nRoll the dice? (y/n): ").strip().lower()

    if choice == "y":
        # Roll two dice
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        print("\n--------------------")
        print(f"🎲 Die 1: {d1}")
        print(f"🎲 Die 2: {d2}")

        # Calculate the total
        total = d1 + d2
        print(f"🎯 Total: {total}")

        # Update game statistics
        roll_counter += 1
        best_roll = max(best_roll, total)

        print(f"🏆 Best Roll: {best_roll}")
        print(f"🎲 Rolls: {roll_counter}")

        # Check special combinations
        if d1 == d2:
            print("🎉 Double!")

        if d1 == 1 and d2 == 1:
            print("🐍 Snake Eyes!")

        if total == 7:
            print("🍀 Lucky 7!")

        if total == 12:
            print("💥 Boxcars!")

    elif choice == "n":
        print("\n===== Game Over =====")
        print(f"🎲 Total Rolls: {roll_counter}")
        print(f"🏆 Best Roll: {best_roll}")
        print("Thanks for playing! 🎲")
        break

    else:
        print("❌ Invalid input. Please enter 'y' or 'n'.")

