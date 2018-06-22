package Q8;

public class Main {
    public static void main(String[] args) {
        final double DISCOUNT = .15;
        String priceInString;
        priceInString = "9.99";
        double priceInDouble;
        priceInDouble = Double.parseDouble(priceInString);  // this is where your code will go
        double total;
        total = priceInDouble - (priceInDouble * DISCOUNT);
        System.out.println("The total including discount is: " + total);
    }
}
