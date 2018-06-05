/*
*     Create a number of Rectangle objects from user input lengths and width,
*     and add them to list of rectangles
*     @author Hunter S. Carlisle
 */

package test;

import java.util.ArrayList;
import java.util.Scanner;

public class TestRectangle {
    public static void main(String[] args) {
        // Initialize variables
        Scanner scnr = new Scanner(System.in);
        final int NUMBER_OF_RECTANGLES = 4;
        ArrayList<Rectangle> rectangleArray = new ArrayList<>();
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
        // initialize variable
        int userWidth;
        // get user input
        do {
        System.out.print("Input the width of your rectangle: ");
        userWidth = scnr.nextInt();
        } while (userWidth <= 0);
        return userWidth;
    }

    private static int getUserLength(Scanner scnr) {
        // initialize variable
        int userLength;
        // get user input
        do {
            System.out.print("Input the length of your rectangle: ");
            userLength = scnr.nextInt();
        } while (userLength <= 0);
        return userLength;
    }
}


/*
*    ====== OUTPUT ======
*    Input the length of your rectangle: 10
*    Input the width of your rectangle: 10
*
*    Input the length of your rectangle: 0
*    Input the length of your rectangle: 10
*    Input the width of your rectangle: 5
*
*    Input the length of your rectangle: -5
*    Input the length of your rectangle: 5
*    Input the width of your rectangle: 0
*    Input the width of your rectangle: 10
*
*    Input the length of your rectangle: 100
*    Input the width of your rectangle: -100
*    Input the width of your rectangle: 100
*
*    [For this Rectangle: length = 10, and width = 10, For this Rectangle: length = 10, and width = 5, For this Rectangle: length = 5, and width = 10, For this Rectangle: length = 100, and width = 100]*
*/

