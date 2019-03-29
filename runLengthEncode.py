'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

testEncode = "AAAABBBCCDAA"
testDecode = "4A3B2C1D2A"


def rLEncode(code, type):
    output = ""
    copyOfcode = code
    if(type == "Encode"):
        char = ""
        charCount = 0
        while(copyOfcode):
            if char == '':
                char = copyOfcode[0]
                charCount += 1
            elif char != copyOfcode[0]:
                output += str(charCount) + char
                char = copyOfcode[0]
                charCount = 1
            else:
                charCount += 1
            copyOfcode = copyOfcode[1:]
        output += str(charCount) + char
    if(type == "Decode"):
        while(copyOfcode):
            output += copyOfcode[1] * int(copyOfcode[0])
            copyOfcode = copyOfcode[2:]
    return output

print(rLEncode(testEncode, "Encode"))
print(rLEncode(testDecode, "Decode"))