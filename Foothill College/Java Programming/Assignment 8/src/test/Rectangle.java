package test;

/**
 * One object of this class represents a rectangle's length and width.
 */
public class Rectangle {
    private int length;
    private int width;
    /**
     * returns the length of the Rectangle object
     */

    public int getLength() {
        return this.length;
    }
    /**
     * sets the length of the Rectangle to "newLength"
     */
    public void setLength(int newLength) {
        this.length = newLength;
    }
    /**
     * returns the width fo the Rectangle object
     */
    public int getWidth() {
        return this.width;
    }
    /**
     * Sets the width of the Rectangle to "newWidth"
     */
    public void setWidth(int newWidth) {
        this.width = newWidth;
    }
    /**
     * Returns a String containing the length and
     * width of the Rectangle.
     */
    public String toString() {
        return "For this Rectangle: length = " + this.length + ", and width = " + this.width;
    }
}