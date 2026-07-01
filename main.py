import random

fav_language = []

lang1= input("Enter your 1st favourite language: ")
fav_language.append(lang1)

lang2 = input("Enter your 2nd favourite language: ")
fav_language.append(lang2)

lang3 = input("Enter your 3rd favourite language: ")
fav_language.append(lang3)


def choosing_lucky_language(lang_list):
	lucky = random.choice(lang_list)
	return lucky


picked_up = choosing_lucky_language(fav_language)
print(f"Bhai, aaj aapko {picked_up} par kaam krna chahiye")

