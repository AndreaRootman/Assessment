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

if show_instructions == "yes":
    print("program continues")

elif show_instructions == "no":
    print("Display instructions")
    print(f"\nSo {name}, in this quiz I will give you a word in Te Reo Maori.\n"
          f"\n You must answer the question in English, your answer could be the number or the word, good luck.\n")

else:
    print("please answer 'yes or 'no' ")

print(f"entered '{show_instructions}' ")







