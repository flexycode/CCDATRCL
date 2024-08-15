public class DivisibleBy3And5 {
    public static void main(String[] args) {
        // Loop through numbers from 1 to 100
        for (int i = 1; i <= 100; i++) {
            // Check if the current number is divisible by both 3 and 5
            if (i % 3 == 0 && i % 5 == 0) {
                // If it's divisible by both, print the number
                System.out.println(i);
            }
        }
    }
}