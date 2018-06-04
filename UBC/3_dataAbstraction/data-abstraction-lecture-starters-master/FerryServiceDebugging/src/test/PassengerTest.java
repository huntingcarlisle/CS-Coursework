<<<<<<< HEAD
package test;

import model.Passenger;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class PassengerTest {

    private Passenger testPassenger;

    @Before
    public void setUp() {
        testPassenger = new Passenger("Bruce Wayne");
    }

    @Test
    public void testPassengerConstructor() {
        assertEquals(testPassenger.getName(), "Burce Wayne");
        assertEquals(testPassenger.getFerryCard().getOwner(), testPassenger);
    }

    @Test
    public void testPassengerChangeName() {
        testPassenger.setName("Batman");
        assertEquals("Batman",testPassenger.getName());
    }

=======
package test;

import model.Passenger;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class PassengerTest {

    private Passenger testPassenger;

    @Before
    public void setUp() {
        testPassenger = new Passenger("Bruce Wayne");
    }

    @Test
    public void testPassengerConstructor() {
        assertEquals(testPassenger.getName(), "Burce Wayne");
        assertEquals(testPassenger.getFerryCard().getOwner(), testPassenger);
    }

    @Test
    public void testPassengerChangeName() {
        testPassenger.setName("Batman");
        assertEquals("Batman",testPassenger.getName());
    }

>>>>>>> c498588a1dd2b283d94f914254371a58e9d8d989
}