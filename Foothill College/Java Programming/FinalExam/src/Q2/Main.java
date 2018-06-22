package Q2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your age?");
        int age;
        age = scanner.nextInt();
//        System.out.println(age);
// your if/else statement will be added right here
        if (age >= 13 && age < 20) {
            System.out.println("you are a teenager");
        }
        else {
            System.out.println("you are not a teenager");
        }
    }
}
