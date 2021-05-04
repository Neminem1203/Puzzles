roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}

def romanToDec(roman):
    sum = roman_val[roman[-1]]
    ind = 0
    while ind < len(roman)-1:
        char = roman[ind]
        val = roman_val[char]
        next_val = roman_val[roman[ind+1]]
        if next_val <= val:
            sum += val
        else:
            sum -= val
        ind += 1
    return sum

         # 4      49       83        94      2021     86
romans = ["IV", "XLIX", "LXXXIII", "XCIV", "MMXXI", "LXXXIV"]

for roman in romans:
    print(romanToDec(roman))