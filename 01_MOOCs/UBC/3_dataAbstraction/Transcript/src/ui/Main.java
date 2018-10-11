package ui;

import model.Transcript;

public class Main {
    public static void main(String[] args){
        Transcript t1 = new Transcript("Hunter Carlsle", 104076514);
        Transcript t2 = new Transcript("Ada Lovelace", 8853);
        Transcript t3 = new Transcript("Katie White", 1234567);

        t1.addGrade("Phil 100C", 4.0);
        t1.addGrade("Math 32A", 3.7);
        t2.addGrade("CPSC-110", 3.1);
        t3.addGrade("WS 101", 4.0);



        System.out.print(t1.getStudentName() + ": ");
        t1.printTranscript();

        System.out.println(t1.getGPA());


        System.out.print(t3.getStudentName() + ": ");
        t3.printTranscript();

        System.out.println(t3.getGPA());

    }
}
