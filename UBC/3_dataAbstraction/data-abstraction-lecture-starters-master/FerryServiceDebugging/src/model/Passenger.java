<<<<<<< HEAD
package model;

public class Passenger {

    private String name;
    private FerryCard ferryCard;

    public Passenger(String name) {
        this.name = name;
        FerryCard ferryCard = new FerryCard();
        setFerryCard(ferryCard);
        ferryCard.setOwner(this);
    }

    // getters
    public String getName() { return name; }
    public FerryCard getFerryCard() { return ferryCard; }

    //MODIFIES: this
    //EFFECTS: sets name to parameter
    public void setName(String name) {
        this.name = name;
    }

    //MODIFIES: this
    //EFFECTS: sets ferry card to parameter
    public void setFerryCard(FerryCard ferryCard) {
        this.ferryCard = ferryCard;
    }


=======
package model;

public class Passenger {

    private String name;
    private FerryCard ferryCard;

    public Passenger(String name) {
        this.name = name;
        FerryCard ferryCard = new FerryCard();
        setFerryCard(ferryCard);
        ferryCard.setOwner(this);
    }

    // getters
    public String getName() { return name; }
    public FerryCard getFerryCard() { return ferryCard; }

    //MODIFIES: this
    //EFFECTS: sets name to parameter
    public void setName(String name) {
        this.name = name;
    }

    //MODIFIES: this
    //EFFECTS: sets ferry card to parameter
    public void setFerryCard(FerryCard ferryCard) {
        this.ferryCard = ferryCard;
    }


>>>>>>> c498588a1dd2b283d94f914254371a58e9d8d989
}