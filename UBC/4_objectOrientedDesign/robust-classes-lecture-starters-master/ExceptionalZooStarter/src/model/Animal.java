package model;

import exceptions.NotHungry;

public class Animal {

    private boolean isHungry = false;
    private boolean hungry;
    private int eaten = 0;

    // getters
    public boolean isHungry() { return hungry; }

    public int eat() throws NotHungry {
        if(!isHungry) {
            throw new NotHungry();
        }
        isHungry = false;
        eaten++;
        return eaten;
    }


}