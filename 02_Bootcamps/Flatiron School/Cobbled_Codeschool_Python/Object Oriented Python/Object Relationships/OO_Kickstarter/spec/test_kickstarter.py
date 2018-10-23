"""
This program contains all units tests Backer and Project classes.
"""

import unittest

from lib.project import Project
from lib.backer import Backer


class TestKickstarter(unittest.TestCase):

    def setUp(self):
        """setUp function for Backer unit tests """
        self.b1 = Backer("Avi")
        self.b2 = Backer("Spencer")

        self.p1 = Project("Project With So Much Amaze")
        self.p2 = Project("Magic The Gathering Thing")

    def test_backerHasName(self):
        """ Unit test for Backer.__init__ errors """
        self.assertEqual(self.b1.getName(), "Avi")

    def test_projectHasTitle(self):
        """ Unit test for Project.__init__ errors """
        self.assertEqual(self.p1.getTitle(), "Project With So Much Amaze")

    def test_backProject(self):
        """ Unit test for Backer.backProject"""
        self.b2.backProject(self.p1)
        self.assertTrue(self.p1 in self.b2.getProjects())
        # Advanced
        self.assertTrue(self.b2 in self.p1.getBackers())

    def test_addBacker(self):
        """ Unit test for Project.addBacker"""
        self.p2.addBacker(self.b1)
        self.assertTrue(self.b1 in self.p2.getBackers())
        # Advanced
        self.assertTrue(self.p2 in self.b1.getProjects())

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
===== OUTPUT =====

"""