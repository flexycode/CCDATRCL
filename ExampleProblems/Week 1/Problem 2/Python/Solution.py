# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Check if the current number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        # If it's divisible by both, print the number
        print(i)