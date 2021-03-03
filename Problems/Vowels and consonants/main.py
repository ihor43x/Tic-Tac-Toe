user_input = input()
for c in user_input:
    if not c.isalpha():
        break
    print("vowel" if c in "aeiou" else
          "consonant")