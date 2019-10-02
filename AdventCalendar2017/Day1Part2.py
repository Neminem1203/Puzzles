def sumOfCaptcha(captcha):
    captcha = captcha.strip()
    sum = 0
    n = len(captcha)
    step = int(n/2)
    print("Captcha: ",captcha)
    for i in range(n):
        if captcha[i] == captcha[(i+step)%n]:
            sum += int(captcha[i])
    return sum

f = open("input.txt", "r")
contents = f.readlines()

for num in contents:
    print(sumOfCaptcha(num))