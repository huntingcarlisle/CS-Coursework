/*
* One object of class Employee represents one employee
*
* Author: Hunter S. Carlisle
 */

package models;

public class Employee {
    private String firstName;
    private String lastName;
    private int socialSecurityNumber;
    private double currentSalary;

    // Constructors
    public Employee(){
        // Initialize Employee object with no parameters.
        this.firstName = "";
        this.lastName = "";
        this.socialSecurityNumber = 0;
        this.currentSalary = 0.0;
    }
    public Employee(String firstName, String lastName, int socialSecurityNumber, double baseSalary){
        /*
        Initialize Employee object with parameters, as follows:

        firstName (String): Employee's first name
        lastName (String): Employee's last name
        socialSecurityNumber (int): Employee's government issued SSN
        baseSalary (double): Employee's starting salary upon initialization
         */
        this.firstName = firstName;
        this.lastName = lastName;
        this.socialSecurityNumber = socialSecurityNumber;
        this.currentSalary = baseSalary;
    }

    // getters
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public int getSocialSecurityNumber() { return socialSecurityNumber; }
    public double getSalary() { return currentSalary; }

    // setters
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public void setSocialSecurityNumber(int socialSecurityNumber) { this.socialSecurityNumber = socialSecurityNumber; }
    public void setSalary(double baseSalary) { this.currentSalary = baseSalary; }

    // Public Methods
    public String toString(){
        // Print employee object information as a string sentence.
        return (this.firstName + " " + this.lastName + " is an employee of the firm whose social security number is " + this.socialSecurityNumber + " and salary is " + this.currentSalary);
    }

    public void giveRaise(double percentRaise) {
        // EFFECTS: Increase salary by an input
        // REQUIRES: percent raise should be double between 0.0 and 1.0
        currentSalary *= 1.0 + percentRaise;
    }
}
