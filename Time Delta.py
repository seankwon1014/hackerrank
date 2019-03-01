import math
import os
import random
import re
import sys

# Complete the time_delta function below.
import datetime as dt
import time
def time_delta(t1, t2):
    dct = {}
    for i in (t1, t2):
        x2 = i.split(' ')
        x3 = ' '.join(x2[1:5])
        x4 = dt.datetime.strptime(x3, '%d %b %Y %H:%M:%S')
        xa = time.mktime(x4.timetuple())

        x5 = x2[5:]
        x6 = (x5[0][:-4]), str(int(x5[0][-4:-2]) * 3600 + int(x5[0][-2:]) * 60)
        xb = int(''.join(x6)) * -1
        dct[i] = int(xa + xb)
    return str(abs(dct[t1] - dct[t2]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
