'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

def sentenceReconstruction(dictionary, sentence):
    returnSentence = []
    while(sentence):
        wordRemoved = False
        for i in dictionary:
            if i == sentence[:len(i)]:
                returnSentence.append(i)
                sentence = sentence[len(i):]
                wordRemoved = True
                break
        if(not wordRemoved):
            return None
    return returnSentence

dict = ['bed', 'bath', 'bedbath', 'and', 'beyond', 'quick', 'brown', 'the', 'fox']
sent =      "bedbathandbeyond"
fakesent =  "bedbatandbeyond"
theQBF =    "thequickbrownfox"
print(sentenceReconstruction(dict, sent))
print(sentenceReconstruction(dict, fakesent))
print(sentenceReconstruction(dict, theQBF))
