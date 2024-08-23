def is_palindrome(s):
    """
    Returns True if the input string is a palindrome, False otherwise.
    """
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# Ask the user to input a string
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    
    # If it's a palindrome, print a message
    print("The string is a palindrome.")
else:
    
    # If it's not a palindrome, print a message
    print("The string is not a palindrome.")
