min_, max_, sleep = int(input()), int(input()), int(input())
if sleep < min_:
    print("Deficiency")
elif sleep > max_:
    print("Excess")
else:
    print("Normal")