package ui;

import model.IntegerSet;

public class IntegerSetUsage {
    public static void main(String[] args) {
        IntegerSet mySet = new IntegerSet();
        mySet.insert(3);
<<<<<<< HEAD
        System.out.println("Does the set contain number 3? " + mySet.contains(3));
        System.out.println("The size of the set is: " + mySet.size());
        mySet.remove(3);
        System.out.println("Does the set contain number 3? " + mySet.contains(3));
        System.out.println("The size of the set is: " + mySet.size());
=======
        mySet.remove(3);
>>>>>>> c498588a1dd2b283d94f914254371a58e9d8d989
    }
}
