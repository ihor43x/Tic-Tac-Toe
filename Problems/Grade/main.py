score, maximum = int(input()), int(input())
percent = score / maximum * 100
if percent < 60:
    print("F")
elif percent < 70:
    print("D")
elif percent < 80:
    print("C")
elif percent < 90:
    print("B")
else:
    print("A")