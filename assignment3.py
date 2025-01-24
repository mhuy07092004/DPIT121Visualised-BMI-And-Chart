import unittest


from assignment3 import Person, DietTracker


class TestPerson(unittest.TestCase):
    def test_valid_person(self):
#       Test Male
        male = Person(15, "male",70, 185)
        male.validate()
        self.assertEqual(male.age, 15)
        self.assertEqual(male.gender, "male")
        self.assertEqual(male.weight, 70)
        self.assertEqual(male.height, 185)

#       Test Female
        female = Person(24, "female", 45, 155)
        female.validate()
        self.assertEqual(female.age, 24)
        self.assertEqual(female.gender, "female")
        self.assertEqual(female.weight, 45)
        self.assertEqual(female.height, 155)


    def test_invalid_age(self):
    # Test the Person class for invalid age input
        invalid_ages = [-1, 0, 120, 150]
        for age in invalid_ages:
            with self.assertRaises(ValueError):
                person = Person(age, "male" ,55,170)
                person.validate()
    # Test the person gender invalid input
    def test_invalid_gender(self):
        """Test the Person class for invalid gender input"""
        with self.assertRaises(ValueError):
            person = Person(25, "Gmail", 65,190)
            person.validate()
    def test_invalid_weight(self):
        """Test the Person class for invalid gender input"""
        with self.assertRaises(ValueError):
            person = Person(25, "male", 250,190)
            person.validate()
    def test_invalid_height(self):
        """Test the Person class for invalid gender input"""
        with self.assertRaises(ValueError):
            person = Person(25, "male", 160,1)
            person.validate()

class TestDietTracker(unittest.TestCase):
    def test_valid_diet_input(self):
        male_diet = DietTracker(5, 4,4, 3,2,27.46)
        male_diet.validate()
        self.assertEqual(male_diet.daily_vegetables, 5)
        self.assertEqual(male_diet.daily_fruits, 4)
        self.assertEqual(male_diet.daily_grains, 4)
        self.assertEqual(male_diet.daily_meats, 3)
        self.assertEqual(male_diet.daily_dairy, 2)
        self.assertEqual(male_diet.bmi,27.46)

    def test_invalid_diet(self):
        """Test the Person class for invalid gender input"""
        invalid_input = [-1, 0, 45]
        for vegetables in invalid_input:
            with self.assertRaises(ValueError):
               user_input  = DietTracker(vegetables, 10, 2,3,4)
                DietTracker.validate()
