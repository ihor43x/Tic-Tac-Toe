money = int(input())
if money >= 6769:
    print(f"{money // 6769} sheep")
elif money >= 3848:
    print("1 cow")
elif money >= 1296:
    print("1 pig" if money // 1296 == 1 else f"{money // 1296} pigs")
elif money >= 678:
    print(f"{money // 678} goat")
elif money >= 23:
    print("1 chicken" if money // 23 == 1 else f"{money // 23} chickens")
else:
    print("None")
