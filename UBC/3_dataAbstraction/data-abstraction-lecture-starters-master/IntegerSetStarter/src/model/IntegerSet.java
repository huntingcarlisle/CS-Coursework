package model;

import java.util.ArrayList;

public class IntegerSet {
    ArrayList<Integer> internalArray;

    public IntegerSet() {
        internalArray = new ArrayList<Integer>();
    }

    // MODIFIES: this
    // EFFECTS: inserts integer into set unless it's already there, in which case do nothing.
    public void insert(Integer num) {
        if (!internalArray.contains(num)) {
            internalArray.add(num);
        }
    }

    // MODIFIES: this
    // EFFECTS: if the integer is in the integer set, then remove it from the integer set.
    //          otherwise, do nothing.
    public void remove(Integer num) {

    }

}