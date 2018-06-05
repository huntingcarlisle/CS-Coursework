/*
*     Create a number of Rectangle objects from user input lengths and width,
*     and add them to list of rectangles
*     @author Hunter S. Carlisle
 */

package test;

import java.util.ArrayList;
import java.util.Scanner;

public class TestRectangle_Revised {
    public static void main(String[] args) {
        /*
        Generate a list of rectangles and print to console
         */

        //Initialize variables
        Scanner scnr = new Scanner(System.in);
        final int NUMBER_OF_RECTANGLES = 4;
        ArrayList<Rectangle> rectangleArray = new ArrayList<Rectangle>();

        // Create and store Rectangle objects
        for (int i = 0; i < NUMBER_OF_RECTANGLES; i++) {
            // Instantiate rectangle object
            Rectangle userRectangle = new Rectangle();
            userRectangle.setLength(getUserLength(scnr));
            userRectangle.setWidth(getUserWidth(scnr));
            // Add Rectangle object to array of rectangles
            rectangleArray.add(userRectangle);

            System.out.println();
        }
        System.out.print(rectangleArray);
    }

    private static int getUserWidth(Scanner scnr) {
        /*
        Gets and returns user input width
         */

        System.out.print("Input the width of your rectangle: ");
        return scnr.nextInt();
    }

    private static int getUserLength(Scanner scnr) {
        /*
        Gets and returns user input length
         */

         System.out.print("Input the length of your rectangle: ");
         return scnr.nextInt();
    }
}



/*  ====== OUTPUT ======
Input the length of your rectangle: 1
Input the width of your rectangle: 2

Input the length of your rectangle: 3
Input the width of your rectangle: 4

Input the length of your rectangle: 5
Input the width of your rectangle: 6

Input the length of your rectangle: 7
Input the width of your rectangle: 8

[For this Rectangle: length = 1, and width = 2, For this Rectangle: length = 3, and width = 4, For this Rectangle: length = 5, and width = 6, For this Rectangle: length = 7, and width = 8]
*/


