package model;

import java.util.ArrayList;

public class HairSalon {

    private SpecialistSuggester specialistSuggester;
    private BookingsManager bookingsManager;

    // EFFECTS: creates a hair salon with available booking times from 0-17hrs.
    public HairSalon(){
        specialistSuggester = new SpecialistSuggester();
        bookingsManager = new BookingsManager();
    }

    // MODIFIES: this and Customer
    // EFFECTS:  books the customer into the requested timeslot if it is a valid timeslot, and let's the Customer know the booking time.
    public boolean makeNewBooking(Customer c, int bookingTime, Treatment treatment){
        return bookingsManager.makeNewBooking(c, bookingTime, treatment);
    }

    public boolean cancelBooking(Customer c, int bookingTime, Treatment treatment){
        return bookingsManager.cancelBooking(c, bookingTime, treatment);
    }

    // EFFECTS: prints out all the bookings.  If the time has not been booked, prints "available"
    public void printBookingsList() {
        bookingsManager.printBookingsList();
    }

    // EFFECTS: returns true if the customer is found at the booking time.
    public boolean verifyBooking(Customer c, int bookingTime) {
        return bookingsManager.verifyBooking(c, bookingTime);
    }

    // EFFECTS: returns true if the customer is booked at the booking time
    public boolean confirmBookedName(String cName, int bookingTime){
        return bookingsManager.confirmBookedName(cName, bookingTime);
    }

    // MODIFIES: this and Customer
    // EFFECTS:  changes the customer booked in the bookings, and
    //           lets the Customer know the new booking time.
    public void changeBooking(Customer customer, int newTime){
        bookingsManager.changeBooking(customer, newTime);
    }

    public ArrayList<String> suggestConsultant(Treatment treatment) {
        return specialistSuggester.suggestConsultant(treatment);
    }


}