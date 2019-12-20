# -*- coding: utf8 -*-

print('BWA BWAAA !')

quotes = [ "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
"On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks","Babar","betty boop","calimero","casper","le chat potté", "Kirikou"]


def get_random_item_in(list):
	item = list[1]
	return item

print(get_random_item_in(quotes))

for i in range(len(characters)):
    characters[i] = characters[i].capitalize()

print(characters)

# user_answer = input("Tapez une lettre")
# if user_answer == "B":
# 	print("Ok je m'en vais... pfff")
# 	exit()
# elif user_answer == "C":
#     print("C pas la bonne réponse ! Et G pas d’humour, je C...")
