import sys


# Enter your code here. Read input from STDIN. Print output to STDOUT

def removeSymbolsAndLower(words):
    return_list = []
    for word in words:
        new_word = ""
        for char in word:
            if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z"):
                new_word += char
        return_list += [new_word.lower()]
    return return_list


def matchTitleDescription(n, titles, descriptions):
    common_words = ["who", "what", "when", "where", "why", "how", "the", "of", "to", "be", "and", "a"]
    type = ["Paperback", "Hardcover"]
    words_in_titles = []
    for title in titles:
        words = title.split(" ")
        word_list = removeSymbolsAndLower(words)
        while "" in word_list:
            word_list.remove("")
        words_in_titles += [word_list]

    for description in descriptions[1:]:
        scores = [0 for _ in range(n)]
        words = description.split(" ")
        word_list = removeSymbolsAndLower(words)
        while "" in word_list:
            word_list.remove("")
        for word in word_list:
            if word in common_words:
                continue
            lower_word = word.lower()
            for ind in range(n):
                if lower_word in words_in_titles[ind]:
                    scores[ind] += 1
        high_score = 0
        high_score_ind = -1
        for score_ind in range(len(scores)):
            score = scores[score_ind]
            if score > high_score:
                high_score = score
                high_score_ind = score_ind
        print(high_score_ind + 1)
    return


if __name__ == "__main__":
    counter = 0  # Counter for parsing the titles then description
    titles = []  # list of titles
    descriptions = []  # list of descriptions
    for linenum, line in enumerate(sys.stdin):  # parsing the input
        if linenum == 0:  # getting n
            n = int(line)
            counter = int(line)
            continue
        if counter > 0:  # titles
            counter -= 1
            titles += [line.strip()]
        else:  # descriptions
            descriptions += [line.strip()]

    matchTitleDescription(n, titles, descriptions)
