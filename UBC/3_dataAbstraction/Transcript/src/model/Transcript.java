package model;

import java.util.List;

public class Transcript {

    /**
     * INVARIANT: course list and grade list are the same size
     * each course has a grade associated, and vice versa, at matching indices
     */

    private String studentName;
    private int studentID;
    private List<String> courseNames;
    private List<Double> courseGrades;

    public Transcript(String studentName, int studentID) {
        this.studentName = studentName;
        this.studentID = studentID;


    }

    // getters
    public String getStudentName(){ return studentName;};
    public int getStudentID(){ return studentID;};

    // REQUIRES: grade is between 0.0 and 4.0, and the course is not null
    // MODIFIES: this
    // EFFECTS: adds course and grade to transcript
    public void addGrade(String course, double grade){ }

    //REQUIRES: a course the student has already taken
    // EFFECTS: returns course name and grade in "course: grade" format
    public String getCourseAndGrade(String course){ return null; }

    // EFFECTS: prints course names with grades earned
    public void printTranscript(){ }

    // EFFECTS: calculates and returns GPA
    public double getGPA(){ return 0.0; }
}
