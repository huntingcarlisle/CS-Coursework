package tests;

import model.Coin;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertFalse;

public class testCoin {
    private Coin coin;

    @Before
    public void setup(){
        coin = new Coin();
    }

    @Test
    public void testFlipHeadsAndTails(){
        int flipCount = 0;
        String lastStatus = "heads";
        for (int i = 0; i < 10; i++) {
            coin.flip();
            String status = coin.checkStatus();
            System.out.print(status);
            if(!(status.equals(lastStatus))) {
                flipCount++;
                lastStatus = status;
            }
        }
        assertFalse(flipCount==0);
    }

    @Test
    public void testNoRunofTenInRow() {
        int longestRun = 0;
        int currentRun = 0;
        String lastStatus = "heads";
        for (int i = 0; i < 100; i++) {
            coin.flip();
            String status = coin.checkStatus();
            if(status.equals(lastStatus)) {
                currentRun++;
                if (currentRun > longestRun) {
                    longestRun = currentRun;
                }
            }
            else {
                lastStatus = status;
                currentRun = 0;
            }
        }
        System.out.print(longestRun);
        assertFalse(longestRun > 10);
    }
}
