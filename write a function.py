n, m = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
c = set([int(x) for x in input().split(' ')])
d = set([int(x) for x in input().split(' ')])
h = 0
for i in b:
    if i in c:
        h += 1
    elif i in d:
        h -= 1
print(h)