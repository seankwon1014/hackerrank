import math

def angle(a,b):
    angle = math.atan(a/b) * 180 / math.pi
    angle = round(angle)
    result = str(angle) + '°'
    return result

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(angle(a,b))
