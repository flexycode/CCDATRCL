def is_palindrome(s):
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Define the string to check
str = "madam"

# Check if the string is a palindrome
if is_palindrome(str):
    # If it's a palindrome, print a message
    print("The string is a palindrome.")
else:
    # If it's not a palindrome, print a message
    print("The string is not a palindrome.")
    