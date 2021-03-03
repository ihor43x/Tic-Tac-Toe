cafes, cats = [], []
while True:
    user_input = input()
    if user_input == "MEOW":
        break
    cafes.append(user_input.split()[0])
    cats.append(int(user_input.split()[1]))
print(cafes[cats.index(max(cats))])
