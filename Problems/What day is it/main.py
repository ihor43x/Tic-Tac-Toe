reference_time = 10.5
offset = int(input())
print("Monday" if reference_time + offset < 0 else
      "Tuesday" if reference_time + offset < 24 else
      "Wednesday")