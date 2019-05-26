import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	
	if w in data:
		return data[w]
	
	elif len(w) == 0:
		return "Oops! Nothing entered.\n"
	
	elif len(get_close_matches(w,data.keys()))>0:
		yn = input( "Did you mean %s instead ? Enter Y if yes, or N if no : " % get_close_matches(w, data.keys())[0])		
		if yn == "Y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yn == "N":
			return "The word doesn't exist. Please double check it."
		else:
			return "Didn't understand your entry."

	else:
		return"The word doesn't exist. Please double check it."

print("You are using Dictionary \n")
n=1
while n:
	print("Press 0 to exit, or ")
	word = input("Enter word: ")
	if word == '0':
		break
	output = translate(word)

	if type(output) == list:
		for item in output:
			print(item)

	else:
		print(output)