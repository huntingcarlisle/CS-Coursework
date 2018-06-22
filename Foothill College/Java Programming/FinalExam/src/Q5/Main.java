import java.util.Scanner;
import static Q4.DigitName.digitName;

public class Main {
    public static void main(String[] args) {
        // Takes user input single digit integer, prints the name of the input digit
        Scanner scanner = new Scanner(System.in);
        System.out.println("Type a single digit: ");
        int userDigit;
        userDigit = scanner.nextInt();
        System.out.println(digitName(userDigit));
    }

}
