def isTriangle(a, b, c):
    if a + b + c == 180:
        return True
    else:
        return False

print(isTriangle(30, 60, 90))
print(isTriangle(10, 10, 20))