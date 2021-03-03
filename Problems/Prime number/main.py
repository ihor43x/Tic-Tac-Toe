number = int(input())
is_prime = "prime" if number > 1 else "not prime"
for n in range(2, number):
    if number % n == 0:
        is_prime = "not prime"
        break
print(f"This number is {is_prime}")
