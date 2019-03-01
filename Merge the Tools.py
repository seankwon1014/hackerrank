def merge_the_tools(string, k):
    n = len(string)
    t = k
    while t <= n:
        x = string[t-k: t]
        y = []
        for i in range(len(x)):
            if x[i] not in y:
                y += x[i]
        y = ''.join(y)
        print(y)
        t += k


if __name__ == '__main__':