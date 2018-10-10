/* Asks user to input positive integer, 
	then prints a random array of size input containing integers between 1 and 10 inclusive */
import java.util.Scanner;
import java.util.Random;

public class Main {
	public static void main(String [] args)	{
		// Initialize variables
		Scanner scnr = new Scanner(System.in);
		Random randGen = new Random();
		int arrayLength;

		// Get positive number of random integers to generate from user
		do {
			System.out.println("How many random integers would you like to generate?");
			arrayLength = scnr.nextInt();    
		} while (arrayLength <= 0);
		scnr.close();
		
		// Initialize empty array of length arrayLength
		int[] randomArray = new int[arrayLength];
		
		// Fill randomArray with random integers[1,10] and print to console
		for (int i = 0; i < arrayLength; ++i) {
			randomArray[i] = randGen.nextInt(10) + 1;
			System.out.print(((i > 0) ? ", " : "") + randomArray[i]);
		}
	}
}

/*    === OUTPUT ===

How many random integers would you like to generate? 
15
2, 5, 10, 2, 1, 10, 7, 7, 9, 1, 5, 9, 2, 7, 1
 
 */

