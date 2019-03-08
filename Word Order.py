from collections import OrderedDict
dc = OrderedDict()
n = input()
for i in range(int(n)):
    x = input()
    if x in dc:
        dc[x] += 1
    else:
        dc[x] = 1
print(len(dc))
c = ""
for i in dc.values():
    c += str(i) + ' '
print(c)