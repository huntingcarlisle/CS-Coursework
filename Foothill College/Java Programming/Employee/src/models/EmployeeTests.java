/*
 * This program tests the methods and fields of the Employee object class
 *
 * Author: Hunter S. Carlisle
 */

package models;

public class EmployeeTests {
    public static void main(String[] args) {
        // Initialize EMployee object using constructor with paramenters
        Employee djt = new Employee("Donald", "Drumpf", 111111111, 30.0);

        //Test getters
        System.out.println(djt.getFirstName());
        System.out.println(djt.getLastName());
        System.out.println(djt.getSocialSecurityNumber());
        System.out.println(djt.getSalary());

        // Test toString Method
        System.out.println(djt.toString());

        // Test giveRaise method
        djt.giveRaise(.01);
        System.out.println(djt.getSalary());

        System.out.println();

        // Initialize Employee Object using constructor with no parameters
        Employee hsc = new Employee();
        System.out.println(hsc.toString());

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
        System.out.println(hsc.toString());

        // Test giveRaise method
        hsc.giveRaise(.40);
        System.out.println(hsc.getSalary());
    }
}


/*
======   OUTPUT   =======
Donald
Drumpf
111111111
30.0
Donald Drumpf is an employee of the firm whose social security number is 111111111 and salary is 30.0
30.3

  is an employee of the firm whose social security number is 0 and salary is 0.0
Hunter
Carlisle
123456789
100000.0
Hunter Carlisle is an employee of the firm whose social security number is 123456789 and salary is 100000.0
140000.0
*/
