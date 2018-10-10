from Q2 import Point
import math


class Line:
    '''
    One object represents a Line between two Point Objects
    '''

    def __init__(self, pointOne, pointTwo):
        '''
        Initializes a Line Object:
        pointOne: the starting point for the line
        pointTwo: the end point of the line
        '''
        self.start = pointOne
        self.end = pointTwo

    def __str__(self):
        '''
        Return a string representation of a line
        '''
        return "A line from " + str(self.start) + " to " + str(self.end)

    def length(self):
        '''
        Return the length of the line
        '''
        return math.sqrt(math.pow((self.start.x - self.end.x), 2) + math.pow((self.start.y - self.end.y), 2))


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(3, 4)
    p3 = Point(1, 11)
    p4 = Point(11,11)
    p5 = Point(-1, -1)
    p6 = Point(-1, 1)

    # test line from origin
    line1 = Line(p1, p2)
    print(line1)
    print(line1.length()) # expect 5.0


    # test horizontal line
    line2 = Line(p3,p4)
    print(line2)
    print(line2.length()) # expect 10.0

    # test vertical line
    line3 = Line(p5, p6)
    print(line3)
    print(line3.length()) # expect 2.0

    # test diagonal line
    line4 = Line(p2, p3)
    print(line4)
    print(line4.length())  # expect 7.28...

