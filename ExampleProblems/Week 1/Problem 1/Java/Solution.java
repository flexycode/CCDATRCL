public class EvenNumbers {
    public static void main(String[] args) {
        // Loop through numbers from 1 to 100
        for (int i = 1; i <= 100; i++) {
            // Check if the current number is even (i.e., divisible by 2)
            if (i % 2 == 0) {
                // If it's even, print the number
                System.out.println(i);
            }
        }
    }
}