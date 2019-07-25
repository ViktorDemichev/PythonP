import json
from difflib import get_close_matches as gcm
data = json.load(open("data.json")) 

word = input("Enter Word \n") 
b_match = gcm(word, data.keys(), n=1)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]

    else: 
        
        print ("This word doesn't exist. Did you mean?")
        print (b_match)

        switch = input("y/n?")
        if switch == "y":
            print (data[''.join(b_match)])
        else:
            return "This word doesn't exist."
        

print(translate(word))
