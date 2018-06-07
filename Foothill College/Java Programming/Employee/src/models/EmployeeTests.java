/*
 * This program tests the methods and fields of the Employee object class
 *
 * Author: Hunter S. Carlisle
 */

package models;

public class EmployeeTests {
    public static void main(String[] args) {
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
        System.out.println(djt.toString());
        System.out.println(bho.toString());

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

Process finished with exit code 0
*/
