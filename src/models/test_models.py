import unittest
from pydantic import BaseModel

from location import Location

class Test(unittest.TestCase):
    def setUp(self):
        pass




    ## Location model
    def test_location(self):
        location = Location(city="London")
        self.assertTrue(hasattr(location, "city"))
        self.assertTrue(hasattr(location, "state"))
        self.assertTrue(hasattr(location, "country"))






if __name__ == '__main__':
    unittest.main()
