
STDIN = input()
STDOUT = ''
n = 1
for i in range(len(STDIN)):
    x = str(STDIN[i])
    if i+1 == len(STDIN):
        STDOUT += ('(' + str(n) + ', ' + str(STDIN[i]) + ')')
    elif STDIN[i] == STDIN[i+1]:
        n += 1
    else:
        STDOUT += ('(' + str(n) + ', ' + str(STDIN[i]) + ') ')
        n = 1
print(STDOUT)