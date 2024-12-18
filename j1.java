import java.util.Scanner;

public class j1 {
    public static void main(String[] args) {
        // Use try-with-resources to automatically close the scanner
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the first number: ");
            double num1 = scanner.nextDouble();

            System.out.print("Enter the second number: ");
            double num2 = scanner.nextDouble();

            // Round both numbers to three decimal places
            num1 = Math.round(num1 * 1000) / 1000.0;
            num2 = Math.round(num2 * 1000) / 1000.0;

            // Compare the numbers with an epsilon for precision tolerance
            double epsilon = 0.0001; // a small tolerance value
            if (Math.abs(num1 - num2) < epsilon) {
                System.out.println("The numbers are the same up to three decimal places.");
            } else {
                System.out.println("The numbers are not the same up to three decimal places.");
            }
        } // The scanner will be automatically closed here
    }
}
