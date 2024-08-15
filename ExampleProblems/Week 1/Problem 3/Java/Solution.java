public class PalindromeCheck {
    public static void main(String[] args) {
        // Define the string to check
        String str = "madam";
        
        // Create a reversed copy of the string
        String reversed = new StringBuilder(str).reverse().toString();
        
        // Check if the original string is equal to the reversed string
        if (str.equals(reversed)) {
            // If they're equal, the string is a palindrome
            System.out.println("The string is a palindrome.");
        } else {
            // If they're not equal, the string is not a palindrome
            System.out.println("The string is not a palindrome.");
        }
    }
}

