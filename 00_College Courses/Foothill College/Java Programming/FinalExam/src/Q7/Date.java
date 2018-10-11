package Q7;

public class Date {
    // One object of class Date represents the month, day, and year for one date on the calendar
    private int month;
    private int day;
    private int year;

    // Constructors
    public Date(){
        this.month = 0;
        this.day = 0;
        this.year = 0;
    }

    // Setters
    public void setMonth(int month) { this.month = month; }
    public void setDay(int day) { this.day = day; }
    public void setYear(int year) { this.year = year; }

    // Public Methods
    public String toString(){
        // Print employee object information as a string sentence.
        return (this.month + "/" + this.day + "/" + this.year);
    }
}
