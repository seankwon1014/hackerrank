if __name__ == '__main__':
    n = int(input())

import math

def read(n):
    x = 0
    a= 0
    for i in range(n):
        a = 10**(math.ceil(math.log(i+2, 10)))
        x *=a
        x += i+1
    return x


print(read(n))

