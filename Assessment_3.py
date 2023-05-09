"""Component 1 - welcome screen and instructions"""

def get_name():
    name_local = input("what is your name: ")
    return name_local

def get_age():
    age_local = int(input("How old are you: "))
    return age_local

name = get_name()
age = get_age()
print(f"\nHello {name}. At {age} years old you may or may not find this quiz a bit easy.\n")

show_instructions = input("Have you played this game before? :")

if show_instructions == "yes" or show_instructions == "y" or show_instructions == "y" or show_instructions == "Yes":
 print("program continues")

elif show_instructions == "no" or show_instructions == "n" or show_instructions == "No":
    print("Display instructions")
    print(f"\nSo {name}, in this quiz I will give you a word in Te Reo Maori.\n"
          f"\n You must answer the question in English, your answer could be the number or the word, good luck.\n")

else:
    print("please answer 'yes or 'no' ")

print(f"entered '{show_instructions}' ")


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


