package ui;
/**
 * One object of this class instantiates a JFrame. It also
 * instantiates a JTextField, a JButton and a JLabel, and
 * adds them to the JFrame
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUIApp implements ActionListener {
    private JFrame myWindow;
    private JTextField userInput;
    private JButton hello;
    private JButton bye;
    private JLabel output;

    /**
     *  constructor sets up the JFrame.
     */
    public GUIApp() {
        setUpWindow();
        setUpEntry();
        setUpHelloButton();
        setUpByeButton();
        setUpOutput();
        myWindow.validate();
    }

    /**
     *  Instantiates a new JFrame and sets it up empty
     */
    public void setUpWindow() {
        myWindow = new JFrame();
        myWindow.setLayout(new FlowLayout());
        myWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myWindow.setSize(300, 150);
        myWindow.setVisible(true);
    }
    /**
     * Instantiates a text entry box for user input and adds it to the JFrame.
     */
    public void setUpEntry() {
        userInput = new JTextField("Type your name here");
        myWindow.add(userInput);
    }

    /**
     * Instantiates a hello button and adds it to the JFrame.
     */
    public void setUpHelloButton() {
        hello = new JButton("Hi");
        myWindow.add(hello);
        hello.addActionListener(this);
    }

    /**
     * Instantiates a goodbye button and adds it to the JFrame.
     */
    public void setUpByeButton() {
        bye = new JButton("Bye");
        myWindow.add(bye);
        bye.addActionListener(this);
    }

    /**
     *  Instantiates a JTextField for displaying the output, adds it to the JFrame
     *  but leaves it empty.
     */
    public void setUpOutput() {
        output = new JLabel("                               ");
        myWindow.add(output);
    }
    /**
     *  Java calls this method when the user clicks the hello or bye buttons.
     *  This makes up a message String and puts it into the output TextField.
     */
    public void actionPerformed(ActionEvent event) {
        if (event.getActionCommand() == "Hi") {
            String usersName = userInput.getText();
            output.setText("Well hello there " + usersName + "!");
        }
        else if (event.getActionCommand() == "Bye") {
            String usersName = userInput.getText();
            output.setText("Goodbye " + usersName + "!");
        }
    }
}

