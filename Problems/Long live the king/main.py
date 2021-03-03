x = int(input())
y = int(input())
if 1 <= x <= 8 and 1 <= y <= 8:
    if 1 < x < 8 and 1 < y < 8:
        print(8)
    elif x in [1, 8] and y in [1, 8]:
        print(3)
    else:
        print(5)
else:
    print("Out of range!")