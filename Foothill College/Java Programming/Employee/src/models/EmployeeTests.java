package models;

public class EmployeeTests {
    public static void main(String[] args) {
        Employee hsc = new Employee();
        Employee djt = new Employee("Donald", "Drumpf", 111111111, 30.0);
        System.out.print(djt.toString());
    }
}
