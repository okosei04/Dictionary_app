import json

data = json.load(open('dic/data.json'))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Please double check the spelling."
    
give_word = input("Enter a word: ")

print(translate(give_word))