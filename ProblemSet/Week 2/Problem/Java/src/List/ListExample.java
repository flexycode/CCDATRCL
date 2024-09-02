package List;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListExample {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Create a List of strings
        List<String> kpop = new ArrayList<>();

        // Ask the user to enter the number of K-POP groups to add to the list
        System.out.print("Enter the number of K-POP groups to add to the list: ");
        int numGroups = scanner.nextInt();

        // Ask the user to enter the K-POP groups to add to the list
        System.out.println("Enter the K-POP groups to add to the list:");
        for (int i = 0; i < numGroups; i++) {
            System.out.print("Group " + (i + 1) + ": ");
            String group = scanner.next();
            kpop.add(group);
        }

        // Print the list elements
        System.out.println("List KPOP:");
        for (String group : kpop) {
            System.out.print(group + " ");
        }
        System.out.println();

        // Ask the user if they want to remove a K-POP group from the list
        System.out.print("Do you want to remove a K-POP group from the list? (yes/no): ");
        String input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Ask the user to enter the K-POP group to remove
            System.out.print("Enter the K-POP group to remove: ");
            String removeGroup = scanner.next();
            kpop.remove(removeGroup);

            // Print the updated list elements
            System.out.println("Updated list KPOP:");
            for (String group : kpop) {
                System.out.print(group + " ");
            }
            System.out.println();
        } else {
            System.out.println("No K-POP group removed from the list.");
        }

        // Ask the user if they want to add another K-POP group to the list
        System.out.print("Do you want to add another K-POP group to the list? (yes/no): ");
        input = scanner.next();

        if (input.equalsIgnoreCase("yes")) {
            // Ask the user to enter the new K-POP group
            System.out.print("Enter the new K-POP group: ");
            String newGroup = scanner.next();
            kpop.add(newGroup);

            // Print the updated list elements
            System.out.println("Updated list KPOP:");
            for (String group : kpop) {
                System.out.print(group + " ");
            }
            System.out.println();
        } else {
            System.out.println("No new K-POP group added to the list.");
        }
    }
}