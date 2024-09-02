package Array;

import java.util.Scanner;

public class Array {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Ask the user to enter the size of the array
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Declare and initialize an array of integers with the specified size
        int[] scores = new int[size];

        // Ask the user to enter the values for the array elements
        System.out.println("Enter the values for the array elements:");
        for (int i = 0; i < size; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            scores[i] = scanner.nextInt();
        }

        // Print the array elements
        System.out.println("Array elements:");
        for (int i = 0; i < scores.length; i++) {
            System.out.print(scores[i] + " ");
        }
        System.out.println();

        // Ask the user if they want to add or remove an element from the array
        System.out.print("Do you want to add or remove an element from the array? (add/remove): ");
        String input = scanner.next();

        if (input.equalsIgnoreCase("add")) {
            // Ask the user to enter the new element
            System.out.print("Enter the new element: ");
            int newElement = scanner.nextInt();

            // Create a new array with the added element
            int[] newArray = new int[scores.length + 1];
            System.arraycopy(scores, 0, newArray, 0, scores.length);
            newArray[scores.length] = newElement;

            // Print the updated array elements
            System.out.println("Updated array elements:");
            for (int i = 0; i < newArray.length; i++) {
                System.out.print(newArray[i] + " ");
            }
            System.out.println();
        } else if (input.equalsIgnoreCase("remove")) {
            // Ask the user to enter the index of the element to remove
            System.out.print("Enter the index of the element to remove: ");
            int index = scanner.nextInt();

            // Create a new array with the removed element
            int[] newArray = new int[scores.length - 1];
            System.arraycopy(scores, 0, newArray, 0, index);
            System.arraycopy(scores, index + 1, newArray, index, scores.length - index - 1);

            // Print the updated array elements
            System.out.println("Updated array elements:");
            for (int i = 0; i < newArray.length; i++) {
                System.out.print(newArray[i] + " ");
            }
            System.out.println();
        }
    }
}