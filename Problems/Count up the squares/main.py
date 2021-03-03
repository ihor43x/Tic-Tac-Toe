numbers = []
while True:
    user_input = int(input())
    numbers.append(user_input)
    if sum(numbers) == 0:
        break
print(sum(n ** 2 for n in numbers))