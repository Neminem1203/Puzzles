import json
from PyDictionary import PyDictionary

dictionary = PyDictionary()
with open("words_dictionary.json") as json_file:
    data = json.load(json_file)
    for i in data:
        if(len(i) > 3):
            if(i[len(i)-3:] == "ate"):
                print(i)
                print(dictionary.meaning(str(i)))
