

"""component 2- Amount of questions the player wants"""
#confirm question amount
def confirm_question_amount(question_number):
    confirm = ""
    while confirm != "Y" and confirm != "n":
        confirm = input(f"\nYou have {question_number}"
                        f"'Y' or 'N': ").upper()
        if confirm == "Y":
            return True

        else:
            return False




error = "Please enter a whole number between 1 and 10\n"
valid = False


while not valid:
    try:
        num_questions = int(input("How many questions would you like to play with from 1 to 10?"))

        if 0 < num_questions <=10:
            print(f"You are playing with {num_questions}")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)





