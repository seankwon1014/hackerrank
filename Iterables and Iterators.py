from itertools import *

N = input()
L = input()
K = input()

txt = L.split()
com = list(combinations(txt, int(K)))

n = 0
for i in range(len(com)):
    if 'a' in com[i]:
        n += 1

print(round(n/len(com), 3))