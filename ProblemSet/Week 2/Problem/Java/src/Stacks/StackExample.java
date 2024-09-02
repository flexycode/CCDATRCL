package Stacks;

import java.util.Scanner;
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Create a Stack of integers
        Stack<Integer> stack = new Stack<>();

        // Ask the user to enter the number of elements to push onto the stack
        System.out.print("Enter the number of elements to push onto the stack: ");
        int numElements = scanner.nextInt();

        // Ask the user to enter the elements to push onto the stack
        System.out.println("Enter the elements to push onto the stack:");
        for (int i = 0; i < numElements; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            int element = scanner.nextInt();
            stack.push(element);
        }

        // Print the stack elements
        System.out.println("Stack elements:");
        System.out.println(stack);

        // Ask the user if they want to pop an element from the stack
        System.out.print("Do you want to pop an element from the stack? (yes/no): ");
        String input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Pop an element from the stack
            int poppedElement = stack.pop();

            // Print the popped element
            System.out.println("Popped element: " + poppedElement);

            // Print the updated stack elements
            System.out.println("Updated stack elements:");
            System.out.println(stack);
        } else {
            System.out.println("No element popped from the stack.");
        }

        // Ask the user if they want to push another element onto the stack
        System.out.print("Do you want to push another element onto the stack? (yes/no): ");
        input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Ask the user to enter the new element
            System.out.print("Enter the new element: ");
            int newElement = scanner.nextInt();
            stack.push(newElement);

            // Print the updated stack elements
            System.out.println("Updated stack elements:");
            System.out.println(stack);
        } else {
            System.out.println("No new element pushed onto the stack.");
        }
    }
}