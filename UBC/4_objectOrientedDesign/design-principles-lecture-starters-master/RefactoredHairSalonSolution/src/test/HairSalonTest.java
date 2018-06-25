package test;

import model.Customer;
import model.HairSalon;
import model.Treatment;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

//note: this is not a totally exhaustive set of tests!
public class HairSalonTest {
    private HairSalon laBelleSalon;
    private Customer elisa;
    private Treatment cut = new Treatment("cut", 1);
    private Treatment colour = new Treatment("colour", 4);

    @BeforeEach
    public void setUp(){
        laBelleSalon = new HairSalon();
        elisa = new Customer("Elisa");
    }


    @Test
    public void testMakeBookingAtAvailableTime(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 15, cut));
        assertTrue(laBelleSalon.verifyBooking(elisa, 15));
        elisa.setBookedTime(15, cut);
    }

    @Test
    public void makeMultipleBookingsOutOfOrderRefactored(){
        Customer bill11 = new Customer("Bill 11");
        boolean bill11Booked = laBelleSalon.makeNewBooking(bill11, 11, cut);
        Customer bob10 = new Customer("Bob 10");
        boolean bob10Booked = laBelleSalon.makeNewBooking(bob10, 10, cut);
        Customer sara9 = new Customer("Sara 9");
        boolean sara9Booked = laBelleSalon.makeNewBooking(sara9, 9, cut);
        Customer jim15 = new Customer("Jim 15");
        boolean jim15Booked = laBelleSalon.makeNewBooking(jim15, 15, cut);
        Customer sven16 = new Customer("bill");
        boolean sven16Booked = laBelleSalon.makeNewBooking(sven16, 16, cut);
        assertTrue(bill11Booked);
        assertTrue(bob10Booked);
        assertTrue(sara9Booked);
        assertTrue(jim15Booked);
        assertTrue(sven16Booked);


        boolean bill11Verified = laBelleSalon.verifyBooking(bill11, 11);
        boolean bob10Verified = laBelleSalon.verifyBooking(bob10, 10);
        boolean sara9Verified = laBelleSalon.verifyBooking(sara9, 9);
        boolean jim15Verified = laBelleSalon.verifyBooking(jim15, 15);
        boolean sven16Verified = laBelleSalon.verifyBooking(sven16, 16);
        assertTrue(bill11Verified);
        assertTrue(bob10Verified);
        assertTrue(sara9Verified);
        assertTrue(jim15Verified);
        assertTrue(sven16Verified);
    }


    @Test public void confirmUnbookedTimeByName(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 15, cut));
        assertTrue(laBelleSalon.verifyBooking(elisa, 15));
        assertTrue(laBelleSalon.confirmBookedName("Elisa", 15));
    }

    @Test
    public void testMakeBookingAtTakenTime(){
        boolean madeBooking = laBelleSalon.makeNewBooking(elisa, 15, cut);
        assertTrue(madeBooking);
        assertTrue(laBelleSalon.verifyBooking(elisa, 15));
        Customer c = new Customer("Standin Customer");
        assertTrue(laBelleSalon.makeNewBooking(c, 15, cut));
        assertTrue(laBelleSalon.verifyBooking(c, 15));
        assertFalse(laBelleSalon.verifyBooking(elisa, 15));
    }

    @Test
    public void testMakeEarliestBooking(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 9, colour));
        assertTrue(laBelleSalon.verifyBooking(elisa, 9));
    }

    @Test
    public void testMakeLatestBooking(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 17, cut));
        assertTrue(laBelleSalon.verifyBooking(elisa, 17));
    }

    @Test public void testCancelBooking(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 9, colour));
        assertTrue(laBelleSalon.verifyBooking(elisa, 9));
        assertTrue(laBelleSalon.cancelBooking(elisa, 9, colour));
        assertFalse(laBelleSalon.verifyBooking(elisa, 9));
    }

    @Test public void testSuggestedSpecialists(){
        assertTrue(laBelleSalon.makeNewBooking(elisa, 12, new Treatment("cut", 1)));
        ArrayList<String> names = laBelleSalon.suggestConsultant(elisa.getTreatment());
        assertTrue(names!=null && names.size()>0);
    }

}
