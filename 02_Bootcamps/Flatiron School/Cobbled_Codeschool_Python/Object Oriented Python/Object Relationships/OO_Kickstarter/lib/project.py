class Project(object):
    """
    One object of class Backer is a representation of one kickstarter project
    """
    # CLASS VARIABLES

    # CLASS METHODS

    def __init__(self, title):
        """
        Initialize a Project object with a title and a list of backers.
        """
        self.title = title
        self.backers = []

    def getTitle(self):
        """
        Safely access self.title outside of the class
        """
        return self.title

    def getBackers(self):
        """
        Safely access self.backers outside of the class
        """
        return self.backers

    def addBacker(self, backer):
        """ Add a backer to the kickstarter """
        self.backers.append(backer)
        backer.projects.append(self)