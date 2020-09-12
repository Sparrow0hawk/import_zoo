import unittest 
from wonderbar.animal import Animal

class TestAnimal(unittest.TestCase):

    def setUp(self) -> None:

        self.test_animal = Animal(name = "lion", keeper = "Walter")

    def test_Animal_name(self):

        animal_name = self.test_animal.get_name()

        self.assertEqual(animal_name, "lion")
        
        self.assertTrue(isinstance(animal_name, str))


    def test_Keeper_name(self):

        keeper_name = self.test_animal.get_keeper()
        
        self.assertEqual(keeper_name, "Walter")
        
        self.assertTrue(isinstance(keeper_name, str))


if __name__ == '__main__':
    unittest.main()