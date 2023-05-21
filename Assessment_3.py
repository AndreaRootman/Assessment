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
          f"\n You must answer the question only in number form, good luck.\n")

else:
    print("please answer 'yes or 'no' ")

print(f"entered '{show_instructions}' ")


"""component 2- Amount of questions the player wants"""
Prompt = None
while Prompt not in ("yes", "y", "n", "no"): #loop until the user inputs a valid answer
        Prompt = input("Do you wish to continue? answer y or n\n")
        if Prompt in ('y', 'yes'):
            state = 2 # switch state to processing state
        elif Prompt in ('n', 'no'): #cancel
            break

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
        break
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


"""component 3 - Te Reo maori numbers"""
import random

question1 = input("What is the number for Tahi?")
answer1 = ("1")

if question1 == answer1:
    print("####CORRECT####")

elif question1 != answer1:
    print("####INCORRECT####")

question2 = input("What is the number for Rua?")
answer2 = ("2")

if question2 == answer2:
    print("####CORRECT####")

elif question2 != answer2:
    print("####INCORRECT####")

question3 = input("What is the number for Toru?")
answer3 = ("3")

if question3 == answer3:
    print("####CORRECT####")

elif question3 != answer3:
    print("####INCORRECT####")

question4 = input("What is the number for Wha?")
answer4 = ("4")

if question4 == answer4:
    print("####CORRECT####")

elif question4 != answer4:
    print("####INCORRECT####")

question5 = input("What is the number for Rime?")
answer5 = ("5")

if question5 == answer5:
    print("####CORRECT####")

elif question5 != answer5:
    print("####INCORRECT####")

question6 = input("What is the number for Ono?")
answer6 = ("6")

if question6 == answer6:
    print("####CORRECT####")

elif question6 != answer6:
    print("####INCORRECT####")

question7 = input("What is the number for Whitu?")
answer7 = ("7")

if question7 == answer7:
    print("####CORRECT####")

elif question7 != answer7:
    print("####INCORRECT####")

question8 = input("What is the number for Waru?")
answer8 = ("8")

if question8 == answer8:
    print("####CORRECT####")

elif question8 != answer8:
    print("####INCORRECT####")

question9 = input("What is the number for Iwa?")
answer9 = ("9")

if question9 == answer9:
    print("####CORRECT####")

elif question9 != answer9:
    print("####INCORRECT####")

question10 = input("What is the number for Tekau?")
answer10 = ("10")

if question10 == answer10:
    print("####CORRECT####")

elif question10 != answer10:
    print("####INCORRECT####")

quest = question1, question2, question3, question4, question5, question6, question7, question8, question9, question10
question = random.choice(quest)
anss = answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10
