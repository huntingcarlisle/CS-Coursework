class Backer(object):
    """
    One object of class Backer is a representation of one kickstarter patron
    """
    # CLASS VARIABLES

    # CLASS METHODS

    def __init__(self, name):
        """
        Initialize a Backer object with a name and a list of projects backed.
        """
        self.name = name
        self.projects = []

    def getName(self):
        """
        Safely access self.name outside of the class
        """
        return self.name

    def getProjects(self):
        """
        Safely access self.projects outside of the class
        """
        return self.projects

    def backProject(self, project):
        self.projects.append(project)
        project.backers.append(self)