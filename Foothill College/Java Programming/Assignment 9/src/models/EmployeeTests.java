/*
 * This program tests the methods and fields of the Employee object class
 *
 * Author: Hunter S. Carlisle
 */

package models;

import java.util.ArrayList;
import java.util.Scanner;

public class EmployeeTests {
    public static void main(String[] args) {
        // EXTRA CREDIT

        /*
        Generate a list of Employee Objects and print to console
         */

        //Initialize variables
        Scanner scnr = new Scanner(System.in);
        final int NUMBER_OF_EMPLOYEES = 4;
        ArrayList<Employee> employeeArray = new ArrayList<Employee>();

        // Create and store Employee objects
        for (int i = 0; i < NUMBER_OF_EMPLOYEES; i++) {
            // Instantiate Employee object
            Employee userEmployee = new Employee();
            userEmployee.setFirstName(getUserFirstName(scnr));
            userEmployee.setLastName(getUserLastName(scnr));
            userEmployee.setSocialSecurityNumber(getUserSSN(scnr));
            userEmployee.setSalary(getUserSalary(scnr));
            // Add Employee object to array of Employees
            employeeArray.add(userEmployee);

            System.out.println();
        }
        System.out.println(employeeArray);

        System.out.println();


        // TESTS
        // Initialize Employee object using constructor with paramenters
        Employee djt = new Employee("Donald", "Drumpf", 111111111, 30.0);
        Employee bho = new Employee("Barack", "Obama", 999999999, 300000.0);

        //Test getters
        System.out.println(djt.getFirstName());
        System.out.println(djt.getLastName());
        System.out.println(djt.getSocialSecurityNumber());
        System.out.println(djt.getSalary());
        System.out.println(bho.getFirstName());
        System.out.println(bho.getLastName());
        System.out.println(bho.getSocialSecurityNumber());
        System.out.println(bho.getSalary());

        // Test toString Method
        System.out.println(djt);
        System.out.println(bho);

        // Test giveRaise method
        djt.giveRaise(.01);
        System.out.println(djt.getSalary());
        bho.giveRaise(.10);
        System.out.println(bho.getSalary());
        bho.giveRaise(.10);
        System.out.println(bho.getSalary());

        System.out.println();

        // Initialize Employee Object using constructor with no parameters
        Employee hsc = new Employee();
        System.out.println(hsc);

        // Test setters
        hsc.setFirstName("Hunter");
        System.out.println(hsc.getFirstName());
        hsc.setLastName("Carlisle");
        System.out.println(hsc.getLastName());
        hsc.setSocialSecurityNumber(123456789);
        System.out.println(hsc.getSocialSecurityNumber());
        hsc.setSalary(100000.0);
        System.out.println(hsc.getSalary());

        // Test toString Method
        System.out.println(hsc);

        // Test giveRaise method
        hsc.giveRaise(.40);
        System.out.println(hsc.getSalary());
    }

    private static String getUserFirstName(Scanner scnr) {
        /*
        Gets and returns user input first name
         */

        System.out.print("Input the first name of the new employee: ");
        return scnr.next();
    }

    private static String getUserLastName(Scanner scnr) {
        /*
        Gets and returns user input last name
         */

        System.out.print("Input the last name of the new employee: ");
        return scnr.next();
    }

    private static int getUserSSN(Scanner scnr) {
        /*
        Gets and returns user input social security number
         */

        System.out.print("Input the social security number of the new employee: ");
        return scnr.nextInt();
    }

    private static double getUserSalary(Scanner scnr) {
        /*
        Gets and returns user input social security number
         */

        System.out.print("Input the salary of the new employee: ");
        return scnr.nextDouble();
    }

}


/*
======   OUTPUT   =======
Input the first name of the new employee: Billy
Input the last name of the new employee: Madison
Input the social security number of the new employee: 999999999
Input the salary of the new employee: 10000000.0

Input the first name of the new employee: Happy
Input the last name of the new employee: Gilmore
Input the social security number of the new employee: 111111111
Input the salary of the new employee: 10000.00

Input the first name of the new employee: Bobby
Input the last name of the new employee: Boucher
Input the social security number of the new employee: 123456789
Input the salary of the new employee: 10.00

Input the first name of the new employee: Mister
Input the last name of the new employee: Deeds
Input the social security number of the new employee: 000000000
Input the salary of the new employee: 10000.00

[Billy Madison is an employee of the firm whose social security number is 999999999 and salary is 1.0E7, Happy Gilmore is an employee of the firm whose social security number is 111111111 and salary is 10000.0, Bobby Boucher is an employee of the firm whose social security number is 123456789 and salary is 10.0, Mister Deeds is an employee of the firm whose social security number is 0 and salary is 10000.0]

Donald
Drumpf
111111111
30.0
Barack
Obama
999999999
300000.0
Donald Drumpf is an employee of the firm whose social security number is 111111111 and salary is 30.0
Barack Obama is an employee of the firm whose social security number is 999999999 and salary is 300000.0
30.3
330000.0
363000.00000000006

  is an employee of the firm whose social security number is 0 and salary is 0.0
Hunter
Carlisle
123456789
100000.0
Hunter Carlisle is an employee of the firm whose social security number is 123456789 and salary is 100000.0
140000.0
*/
