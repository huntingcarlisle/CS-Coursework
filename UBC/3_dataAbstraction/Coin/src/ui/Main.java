package ui;

import model.Coin;

public class Main {
    public static void main(String[] args) {

        Coin coin = new Coin();
        coin.flip();
        System.out.print(coin.checkStatus());

    }
}
