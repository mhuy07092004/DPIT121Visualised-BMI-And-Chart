import unittest
from assignment3 import Person, DietTracker,create_bmi_chart,create_bar_chart,create_bubble_chart,create_line_chart,export_data
import os
from unittest.mock import Mock,patch

# Person class Test
class TestPerson(unittest.TestCase):
    def test_valid_person(self):
#       Test Male User
        male = Person(15, "male",70, 185)
        male.validate()
        self.assertEqual(male.age, 15)
        self.assertEqual(male.gender, "male")
        self.assertEqual(male.weight, 70)
        self.assertEqual(male.height, 185)

#       Test Female User
        female = Person(24, "female", 45, 155)
        female.validate()
        self.assertEqual(female.age, 24)
        self.assertEqual(female.gender, "female")
        self.assertEqual(female.weight, 45)
        self.assertEqual(female.height, 155)

    # Validation input test
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

# Diet Tracker
class TestDietTracker(unittest.TestCase):
    def test_valid_inputs(self):
        # Test that valid inputs pass validation
        try:
            tracker = DietTracker(
                vegetables=10,
                fruits=5,
                grains=8,
                meats=7,
                dairy=6,
                bmi=22.5
            )
            tracker.validate()
        except ValueError:
            self.fail("Valid inputs raised ValueError unexpectedly")

    def test_invalid_vegetables(self):
        # Test vegetables out of valid range
        with self.assertRaises(ValueError):
            tracker = DietTracker(
                vegetables=0,
                fruits=5,
                grains=8,
                meats=7,
                dairy=6,
                bmi=22.5
            )
            tracker.validate()

    def test_invalid_fruits(self):
        # Test fruits out of valid range
        with self.assertRaises(ValueError):
            tracker = DietTracker(
                vegetables=10,
                fruits=20,
                grains=8,
                meats=7,
                dairy=6,
                bmi=22.5
            )
            tracker.validate()

    def test_invalid_grains(self):
        # Test grains out of valid range
        with self.assertRaises(ValueError):
            tracker = DietTracker(
                vegetables=10,
                fruits=5,
                grains=0,
                meats=7,
                dairy=6,
                bmi=22.5
            )
            tracker.validate()

    def test_invalid_meats(self):
        # Test meats out of valid range
        with self.assertRaises(ValueError):
            tracker = DietTracker(
                vegetables=10,
                fruits=5,
                grains=8,
                meats=20,
                dairy=6,
                bmi=22.5
            )
            tracker.validate()

    def test_invalid_dairy(self):
        # Test dairy out of valid range
        with self.assertRaises(ValueError):
            tracker = DietTracker(
                vegetables=10,
                fruits=5,
                grains=8,
                meats=7,
                dairy=0,
                bmi=22.5
            )
            tracker.validate()
# BMI Chart
class TestBMIChart(unittest.TestCase):
    def setUp(self):
        # Temporary output file for testing
        self.test_output = "test_bmi_chart.jpg"

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_chart_creation(self):
        # Test chart creation with a standard BMI
        try:
            create_bmi_chart(25, self.test_output)
            # Check if file was created
            self.assertTrue(os.path.exists(self.test_output))
        except Exception as e:
            self.fail(f"create_bmi_chart() raised {type(e).__name__} unexpectedly!")

    def test_different_bmi_values(self):
        # Test multiple BMI values
        test_bmi_values = [15, 20, 28, 33]
        for bmi in test_bmi_values:
            output_file = f"test_bmi_chart_{bmi}.jpg"
            create_bmi_chart(bmi, output_file)
            self.assertTrue(os.path.exists(output_file))
            # Clean up
            os.remove(output_file)
    # Check If the method called successful
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    def test_chart_methods_called(self, mock_close, mock_savefig):
        # Verify that savefig and close are called
        create_bmi_chart(22, self.test_output)
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()

# Bar Chart
class TestBarChart(unittest.TestCase):
    def setUp(self):
        # Create a mock diet tracker with sample data
        self.mock_diet_tracker = Mock()
        self.mock_diet_tracker.daily_vegetables = 5
        self.mock_diet_tracker.daily_fruits = 2
        self.mock_diet_tracker.daily_grains = 4
        self.mock_diet_tracker.daily_meats = 3
        self.mock_diet_tracker.daily_dairy = 2
        self.test_output = "test_intake_chart.jpg"

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_chart_creation(self):
        # Test chart creation with mock diet tracker
        try:
            create_bar_chart(self.mock_diet_tracker, self.test_output)
            self.assertTrue(os.path.exists(self.test_output))
        except Exception as e:
            self.fail(f"create_bar_chart() raised {type(e).__name__} unexpectedly!")
    # Check If the method called successful
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    def test_chart_methods_called(self, mock_close, mock_savefig):
        # Verify that savefig and close are called
        create_bar_chart(self.mock_diet_tracker, self.test_output)
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()

# Bubble Chart
class TestBubbleChart(unittest.TestCase):
    def setUp(self):
        # Create a mock diet tracker with sample data
        self.mock_diet_tracker = Mock()
        self.mock_diet_tracker.daily_vegetables = 5
        self.mock_diet_tracker.daily_fruits = 2
        self.mock_diet_tracker.daily_grains = 4
        self.mock_diet_tracker.daily_meats = 3
        self.mock_diet_tracker.daily_dairy = 2
        self.test_output = "test_intake_bubble_chart.jpg"

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_chart_creation(self):
        # Test chart creation with mock diet tracker
        try:
            create_bubble_chart(self.mock_diet_tracker, self.test_output)
            self.assertTrue(os.path.exists(self.test_output))
        except Exception as e:
            self.fail(f"create_bubble_chart() raised {type(e).__name__} unexpectedly!")
    # Check If the method called successful
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    def test_chart_methods_called(self, mock_close, mock_savefig):
        # Verify that savefig and close are called
        create_bubble_chart(self.mock_diet_tracker, self.test_output)
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()

class TestLineChart(unittest.TestCase):
    def setUp(self):
        # Create a mock diet tracker with sample data
        self.mock_diet_tracker = Mock()
        self.mock_diet_tracker.daily_vegetables = 5
        self.mock_diet_tracker.daily_fruits = 2
        self.mock_diet_tracker.daily_grains = 4
        self.mock_diet_tracker.daily_meats = 3
        self.mock_diet_tracker.daily_dairy = 2
        self.test_output = "test_intake_line_chart.jpg"

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_chart_creation(self):
        # Test chart creation with mock diet tracker
        try:
            create_line_chart(self.mock_diet_tracker, self.test_output)
            self.assertTrue(os.path.exists(self.test_output))
        except Exception as e:
            self.fail(f"create_line_chart() raised {type(e).__name__} unexpectedly!")
    # Check If the method called successful
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    def test_chart_methods_called(self, mock_close, mock_savefig):
        # Verify that savefig and close are called
        create_line_chart(self.mock_diet_tracker, self.test_output)
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()

# Data Export as Notepad user_info.txt test
class TestDataExport(unittest.TestCase):
    def setUp(self):
        # Create mock objects
        self.mock_person = Mock()
        self.mock_person.age = 30
        self.mock_person.gender = 'male'
        self.mock_person.weight = 75
        self.mock_person.height = 180

        self.mock_diet_tracker = Mock()
        self.mock_diet_tracker.daily_vegetables = 5
        self.mock_diet_tracker.daily_fruits = 2
        self.mock_diet_tracker.daily_grains = 4
        self.mock_diet_tracker.daily_meats = 3
        self.mock_diet_tracker.daily_dairy = 2

        self.test_output = "test_export_data.txt"

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_data_export(self):
        # Export data and verify file creation
        export_data(self.mock_person, self.mock_diet_tracker, self.test_output)
        self.assertTrue(os.path.exists(self.test_output))

    def test_exported_content(self):
        # Export data and verify file contents
        export_data(self.mock_person, self.mock_diet_tracker, self.test_output)

        with open(self.test_output, 'r') as file:
            content = file.read()

        self.assertIn("Age: 30", content)
        self.assertIn("Gender: male", content)
        self.assertIn("Weight: 75 kg", content)
        self.assertIn("Vegetables: 5 servings", content)
        self.assertIn("Fruits: 2 servings", content)
