"""Component 1 - welcome screen and instructions"""

def get_name():
    name_local = input("what is your name: ")
    return name_local
score = 0

def get_age():
    age_local = int(input("How old are you: "))
    return age_local

name = get_name()
age = get_age()
print(f"\nHello {name}. At {age} years old you may or may not find this quiz a bit easy.\n")

show_instructions = input("Have you played this game before? :")

if show_instructions == "yes" or show_instructions == "y" or show_instructions == "Yes":
    print("program continues")

elif show_instructions == "no" or show_instructions == "n" or show_instructions == "No":
    print("Display instructions")
    print(f"\nSo {name}, in this quiz I will give you a word in Te Reo Maori.\n"
          f"\n You must answer the question only in number form, good luck.\n")

else:
    print("please answer 'yes or 'no' or 'y' or 'n'")

print(f"entered '{show_instructions}' ")







