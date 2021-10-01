# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

participant = len(names)

random_selected_participant = random.randint(0, participant)
name_of_random_selected_participant = names[(random_selected_participant-1)]
print(f"{name_of_random_selected_participant} is going to pay meal bill today.")








