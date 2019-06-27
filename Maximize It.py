from sys import stdin
import itertools

A = input().split()
B = stdin.read().splitlines()
K = int(A[0])
M = int(A[1])

def pwr(list):
    return [x**2 for x in list]

ls = {}
for i in range(K):
    ls[i] = list(map(int, B[i].split()))
    del(ls[i][0])
    ls[i] = pwr(ls[i])

dictlist = []
for index in ls:
    dictlist.append(ls[index])

result = list(itertools.product(*dictlist))
sum_tuple = list(map(sum, result))
remain = list(map(lambda x: x%M, sum_tuple))
print(max(remain))
