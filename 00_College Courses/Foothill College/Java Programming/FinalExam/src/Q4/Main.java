package Q4;

public class Main {
    public static void main(String[] args) {
        System.out.println(digitName(7));   // Expects 'four'

    }

    public static String digitName(int digit) {
        // Returns the string containing the name of hte digit sent in as parament
        // digit: integer in set [0,9]
        String name = new String();
        switch (digit) {
            case 0: name = "zero";
                break;
            case 1: name = "one";
                break;
            case 2: name = "two";
                break;
            case 3: name = "three";
                break;
            case 4: name = "four";
                break;
            case 5: name = "five";
                break;
            case 6: name = "six";
                break;
            case 7: name = "seven";
                break;
            case 8: name = "eight";
                break;
            case 9: name = "nine";
                break;
        }
        return name;
    }
}
