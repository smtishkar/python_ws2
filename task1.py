a = float(input("введите a: "))
b = float(input("введите b: "))
c = float(input("введите c: "))

d = b**2 - 4*a * c
if d == 0:
    x = -b / 2*a
    print("x равен - ", x)
else:
    x1 = (-b + d**0.5) / 2 * a
    x2 = (-b - d**0.5) / 2 * a
    print("x1 равен - ", x1)
    print("x2 равен - ", x2)  
