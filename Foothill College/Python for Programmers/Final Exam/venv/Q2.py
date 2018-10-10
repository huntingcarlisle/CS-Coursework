class Point:
    '''
    One object of class Point represents a point in the (x, y) plane
    '''
    def __init__(self, x = 0, y = 0):
        '''
        Initialize a Point Object
        x (integer): The x value of the point
        y (integer): The y value of the point
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Return string representation of a Point as (x,y)
        '''
        return "(" + str(self.x) + "," + str(self.y) + ")"


if __name__ == '__main__':
    # Test no parameters
    p1 = Point()
    print(p1)

    # Test with Parameters
    p2 = Point(2,3)
    print(p2)

    # Test only x parameter
    p3 = Point(x = 4)
    print(p3)

    # Test only y parameter
    p4 = Point(y = 5)
    print(p4)

    # Test negative parameter
    p5 = Point(-2,3)
    print(p5)


