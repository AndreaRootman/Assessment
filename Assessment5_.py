"""Component 5 - Play again?"""
play_again = input(f"Would you like to play again {name}? Please enter either 'yes or no'")
if play_again == 'yes':
    show_instructions
elif play_again == 'no':
    print("Farewell")