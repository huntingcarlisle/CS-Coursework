package model;

public class Airplane implements Flyer, Cafe {
    @Override
    public void serveDrinks() {
        System.out.println("Serving airplane drinks");
    }

    @Override
    public void serveSnacks() {
        System.out.println("Serving airplane snacks.");
        System.out.println("Here are your chips.");
        System.out.println("Here are your peanuts.");
    }

    @Override
    public void takeOff() {
        System.out.println("Taking off!");
    }

    @Override
    public void fly() {
        System.out.println("Flying along -- no turbulence!");
    }

    @Override
    public void land() {
        System.out.println("Fasten your seatbelts - landing!");
    }
}
