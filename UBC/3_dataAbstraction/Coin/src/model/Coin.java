package model;

import java.util.Random;

public class Coin {

    private boolean coinHeadsUp;

    public Coin() {
        coinHeadsUp = false;
    }
    // REQUIRES: nothing
    // MODIFIES: this
    // EFFECTS: generates a random value to set coin value to 0 or 1
    public void flip() {
        Random ran = new Random();
        coinHeadsUp = ran.nextBoolean();
    }

    // REQUIRES: nothing
    // MODIFIES: nothing
    // EFFECTS: returns "heads" if coin value is 0, "tails" if coin value is 1
    public String checkStatus() {
        if (coinHeadsUp) {
            return "heads";
        }
        else {
            return "tails";
        }
    }
}
