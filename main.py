import random

# ASCII art for the game outcomes
rock = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     ________
---'    _____)____
           _______)
          ________)
         ________)
---.___________)
"""

scissors = """
   ________
---'   _____)____
          _______)
       ___________)
      (____)
---.__(___)
"""

# Mapping for user input to ASCII art
options = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# List of outcomes
outcomes = ["It's a tie!", "You lost!", "You won!"]

while True:
    try:
        # Get user input and validate
        user_input = input("Please type your input (Rock/Paper/Scissor) or 'q' to quit:\n").lower()

        if user_input == 'q':
            print("Thanks for playing. Goodbye!")
            break  # Exit the loop if the user inputs 'q'

        if user_input not in options:
            raise ValueError("Please input a valid value")

        # Display user's choice
        print("\nYour Input:\n", options[user_input])

        # Generate random computer output and display corresponding ASCII art
        comp_output = random.randint(0, 2)
        print("\nComputer's Input:")
        print(options["rock" if comp_output == 0 else "paper" if comp_output == 1 else "scissors"])

        # Determine the winner
        result = (comp_output - ["rock", "paper", "scissors"].index(user_input)) % 3
        print(outcomes[result])

    except ValueError as ve:
        print(f"Error: {ve}")

