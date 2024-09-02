package Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class QueueExample {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Create a Queue of strings
        Queue<String> queue = new LinkedList<>();

        // Ask the user to enter the number of elements to add to the queue
        System.out.print("Enter the number of elements to add to the queue: ");
        int numElements = scanner.nextInt();

        // Ask the user to enter the elements to add to the queue
        System.out.println("Enter the elements to add to the queue:");
        for (int i = 0; i < numElements; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            String element = scanner.next();
            queue.add(element);
        }

        // Print the queue elements
        System.out.println("Queue elements:");
        System.out.println(queue);

        // Ask the user if they want to remove an element from the front of the queue
        System.out.print("Do you want to remove an element from the front of the queue? (yes/no): ");
        String input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Remove an element from the front of the queue
            String removedElement = queue.poll();

            // Print the removed element
            System.out.println("Removed element: " + removedElement);

            // Print the updated queue elements
            System.out.println("Updated queue elements:");
            System.out.println(queue);
        } else {
            System.out.println("No element removed from the front of the queue.");
        }

        // Ask the user if they want to add another element to the queue
        System.out.print("Do you want to add another element to the queue? (yes/no): ");
        input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Ask the user to enter the new element
            System.out.print("Enter the new element: ");
            String newElement = scanner.next();
            queue.add(newElement);

            // Print the updated queue elements
            System.out.println("Updated queue elements:");
            System.out.println(queue);
        } else {
            System.out.println("No new element added to the queue.");
        }
    }
}