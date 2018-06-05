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

    // TODO Constructors
    public Employee(){}
    public Employee(String firstName, String lastName, int socialSecurityNumber, double baseSalary){
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

    // EFFECTS: prints employee object information as a string sentence.
    public String toString(){
        return (this.firstName + " " + this.lastName + " is an employee of the firm whose social security number is " + this.socialSecurityNumber + " and salary is " + this.currentSalary);
    }

    // REQUIRES: percent raise should be double between 0.0 and 1.0
    // MODIFIES: this
    // EFFECTS: increases baseSalary by percentRaise
    public void giveRaise(double percentRaise) {
        currentSalary *= 1.0 + percentRaise;
    }


}
