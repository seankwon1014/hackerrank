from itertools import groupby
print(*[(len(list(c)), int(x)) for x, c in groupby(input())])
# x brings each value based on group by
# c brings the location of x: list(c) brings the bunch of x
# if don't use **int** in int(x), it brings string like '1'
