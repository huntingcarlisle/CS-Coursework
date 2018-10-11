package Q6;

import java.awt.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create an ArrayList of three predefined Point Objects and print to console

        // Define an ArrayList of Point objects
        ArrayList<Point> questionSixListOfPoints;
        questionSixListOfPoints = new ArrayList<Point>();

        // Create three new Point objects with the following (x, y) values: (0,6), (4,10), (7,1)
        Point p1 = new Point(0,6);
        Point p2 = new Point(4,10);
        Point p3 = new Point(7,1);

        // Add these three new Point objects to the ArrayList
        questionSixListOfPoints.add(p1);
        questionSixListOfPoints.add(p2);
        questionSixListOfPoints.add(p3);

        // Print the ArrayList to show that the Points are in the list
        System.out.println(questionSixListOfPoints);
    }
}