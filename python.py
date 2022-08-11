for x in range(0, 151): # 1. Basic-range from 0-150
    print(x)

for x in range(5, 1000, 5): # 2. Multiples of Five
    print(x)

for x in range(0, 101): # 3. Counting the Dojo Way
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

sum = 0 # 4. Final sum from 0 to 500,000
for x in range(0, 500001, 2):
    sum += x
print(sum)

for x in range(2018, 0, -4): # 5. Countdown by fours
    print(x)

# 6. Flexible Counter
low = 2
high = 9
mult = 3

for x in range(low, high + 1):
    if x % mult == 0:
        print(x)