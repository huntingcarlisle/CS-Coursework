package Q3;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random;
        random = new Random();
        double[ ] arrayOfDouble;
        final int NUMBER_OF_ELEMENTS = 7;
        arrayOfDouble = new double[NUMBER_OF_ELEMENTS];
        for (int i=0; i < arrayOfDouble.length; i++ ) {
            arrayOfDouble [i] = random.nextInt();
            System.out.println(arrayOfDouble[i]);
        }
// your code will be added right here
        double sumOfArrayOfDouble = 0;
        for (int i=0; i < arrayOfDouble.length; i++) {
            sumOfArrayOfDouble += arrayOfDouble [i];
        }
        System.out.println(sumOfArrayOfDouble);
    }
}
