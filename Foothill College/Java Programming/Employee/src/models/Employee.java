package models;

public class Employee {
    private String firstName;
    private String lastName;
    private int socialSecurityNumber;
    private double baseSalary;

    // TODO Constructors
    public Employee(){}
    public Employee(String firstName, String lastName, int socialSecurityNumber, double baseSalary){
        this.firstName = firstName;
        this.lastName = lastName;
        this.socialSecurityNumber = socialSecurityNumber;
        this.baseSalary = baseSalary;
    }

    // getters
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public int getSocialSecurityNumber() { return socialSecurityNumber; }
    public double getBaseSalary() { return baseSalary; }

    // setters
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public void setSocialSecurityNumber(int socialSecurityNumber) { this.socialSecurityNumber = socialSecurityNumber; }
    public void setBaseSalary(double baseSalary) { this.baseSalary = baseSalary; }

    // EFFECTS: prints employee object information as a string sentence.
    public String toString(){
        return (this.firstName + " " + this.lastName + " is an employee of the firm whose social secuirty number is " + this.socialSecurityNumber + " and salary is " + this.baseSalary);
    }

    // REQUIRES: percentRaise should be double between 0.0 and 1.0
    // MODIFIES: baseSalary
    // EFFECTS: increases baseSalary by percentRaise
    public void giveRaise(double percentRaise) {
        baseSalary *= 1.0 + percentRaise;
    }


}
