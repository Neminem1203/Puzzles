def sumOfCaptcha(captcha):
    captcha = captcha.strip()
    sum = 0
    n = len(captcha)
    print("Captcha: ",captcha)
    for i in range(n):
        if captcha[i] == captcha[(i+1)%n]:
            sum += int(captcha[i])
    return sum

f = open("input.txt", "r")
contents = f.readlines()

for num in contents:
    print(sumOfCaptcha(num))