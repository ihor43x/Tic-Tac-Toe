scores = input().split()
lives = 3
result = 0
for a in scores:
    if lives == 0:
        print("Game over")
        break
    if a == "I":
        lives -= 1
    elif a == "C":
        result += 1
else:
    print("You won")
print(result)