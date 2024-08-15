/**
 * Checks if a given string is a palindrome.
 * 
 * A palindrome is a string that reads the same backward as forward.
 * This class ignores case, spaces, and punctuation when checking for palindromes.
 * 
 * @author [flexycode]
 */

import java.util.Scanner;

public class PalindromeChecker {
  /**
   * Checks if a given string is a palindrome.
   * 
   * This method removes non-alphanumeric characters and converts the string to lowercase
   * before checking if it's a palindrome.
   * 
   * @param s the input string to check
   * @return true if the string is a palindrome, false otherwise
   */
  public static boolean isPalindrome(String s) {
    // Remove non-alphanumeric characters and convert to lowercase
    // This is done to ignore case, spaces, and punctuation when checking for palindromes
    s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

    // Check if the string is equal to its reverse
    // This is the core logic of checking if a string is a palindrome
    String reversed = new StringBuilder(s).reverse().toString();
    return s.equals(reversed);
  }

  /**
   * The main entry point of the program.
   * 
   * This method asks the user to input a string and checks if it's a palindrome.
   * 
   * @param args command-line arguments (not used in this program)
   */
  public static void main(String[] args) {
    // Create a Scanner object to read user input
    Scanner scanner = new Scanner(System.in);

    // Prompt the user to input a string
    System.out.print("Enter a string to check if it's a palindrome: ");

    // Read the user's input
    String inputString = scanner.nextLine();

    // Check if the input string is a palindrome
    if (isPalindrome(inputString)) {
      // If it's a palindrome, print a success message
      System.out.println("The string is a palindrome.");
    } else {
      // If it's not a palindrome, print a failure message
      System.out.println("The string is not a palindrome.");
    }
  }
}
