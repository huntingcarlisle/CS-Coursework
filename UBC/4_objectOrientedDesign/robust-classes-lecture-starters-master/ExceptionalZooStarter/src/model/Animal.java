package model;

import exceptions.AllergyException;
import exceptions.NotHungry;

public class Animal {

    private boolean isHungry = true;
    private boolean isAllergic = true;
    private int eaten = 0;

    // getters
    public boolean isHungry() { return isHungry; }

    public int eat() throws NotHungry, AllergyException {
        if(!isHungry) {
            throw new NotHungry();
        }
        if(isAllergic){
            throw new AllergyException();
        }
        isHungry = false;
        eaten++;
        return eaten;
    }




}