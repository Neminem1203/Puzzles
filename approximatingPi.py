import random
from datetime import datetime
random.seed(datetime.now())

n = 5999999
inside = 0

for i in range(n):
    x = float(random.randint(0,100))/100
    y = float(random.randint(0,100))/100
    if(x**2 + y**2 < 1):
        inside += 1


print(round((inside*4)/n, 3))
