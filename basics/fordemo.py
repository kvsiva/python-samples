# Write a code to print all the values from 1 to 100. Skip the numbers which are divisible by 3 or 5

for i in range(1,101):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)