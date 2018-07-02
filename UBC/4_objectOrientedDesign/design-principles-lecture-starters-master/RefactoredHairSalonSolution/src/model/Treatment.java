package model;


public class Treatment {

    private String name;
    private int hoursNeeded;

    public Treatment(String name, int time) {
        this.name = name;
        this.hoursNeeded = time;
    }

    // getters
    public String getName() { return name; }
    public int getHoursNeeded() { return hoursNeeded; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Treatment)) return false;

        Treatment treatment = (Treatment) o;

        return name.equals(treatment.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }


}