package ui;

import model.*;

public class FlyerDemo {
    public static void main(String[] args) {
        Bird birdie = new Bird();
        Airplane planie = new Airplane();
        Cafe cafePlane = new Airplane();
        Flyer flyerPlane = new Airplane();
        PrivatePlane pp = new PrivatePlane();

        pp.fly();
        pp.bringWarmTowels();
        pp.serveSnacks();

        birdie.fly();
        cafePlane.serveDrinks();

        FlyerDemo fd = new FlyerDemo();
        fd.luxuryTakeoff(pp);
        fd.lunchService(cafePlane);
        fd.firstPartOfFlight(planie);
    }
    public void luxuryTakeoff(PrivatePlane p) {
        p.takeOff();
        p.bringWarmTowels();
    }

    public void lunchService(Cafe c) {
        c.serveDrinks();
        c.serveSnacks();
    }

    public void firstPartOfFlight(Airplane a) {
        a.takeOff();
        a.serveDrinks();
    }
}
