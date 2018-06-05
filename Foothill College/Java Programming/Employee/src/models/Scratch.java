// Task (1): Prints future investment value after 10 years based on input initial investment depoosit
// Task (2): Prints investment value after each year over a 10 year period based on initial deposit

package models;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Scratch {
    public static void main(String[] args) {
        // Initialize variables
        Scanner scnr = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.#");
        final int NUM_TEMPERATURES = 7;
        double[] fahrenheitTemperature = new double[NUM_TEMPERATURES];
        double[] celsiusTemperature = new double[NUM_TEMPERATURES];
        double sum = 0;
        double average;

        // Get input temperatures in fahrenheit, converts to celsius, and add to sum
        for (int i = 0; i < NUM_TEMPERATURES; i++) {
            fahrenheitTemperature[i] = scnr.nextDouble();
            sum += convertToCelsius(fahrenheitTemperature[i]);
            }

        // Calculate average temperature and format decimal
        average = sum / NUM_TEMPERATURES;
        String averageFormatted = df.format(average);

        System.out.println(averageFormatted);
    }

    private static double convertToCelsius(double fahrenheitTemperature) {
        return ((fahrenheitTemperature - 32.0) * (5.0/9.0));
    }
}
