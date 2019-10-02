import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# file = os.path.join(THIS_FOLDER, "input.txt")

def sumOfCaptcha(captcha):
    captcha = captcha.strip()
    sum = 0
    n = len(captcha)
    print("Captcha: ",captcha)
    for i in range(n):
        if captcha[i] == captcha[(i+1)%n]:
            sum += int(captcha[i])
    return sum

# print(file)
f = open("input.txt", "r")
contents = f.readlines()

for num in contents:
    print(sumOfCaptcha(num))