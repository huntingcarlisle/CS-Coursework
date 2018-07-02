from Q2 import Point

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



if __name__ == '__main__':
    p1 = Point()
    p2 = Point(3,4)
    line1 = Line(p1, p2)
    print(line1)
    line1.length()
