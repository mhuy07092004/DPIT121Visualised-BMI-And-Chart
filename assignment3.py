# import matplotlib.pyplot as plt
# import numpy as np

# Person Class Includes Theirs Information
class Person:
    def __init__(self, age, gender, weight, height):
        self.age = age
        self.gender = gender.lower()
        self. weight = weight
        self. height = height
    def validate(self):
        if not (0 < self.age <120):
            raise ValueError("Invalid Age Please Enter Again!")
        if self.gender not in ["male", "female"]:
            raise ValueError("Invalid Gender Please Enter Again!")
        if not (20< self.weight <200):
            raise ValueError("Invalid Weight Please Enter Again!")
        if not (50< self.height <250):
            raise ValueError("Invalid Height Please Enter Again!")

#     Tracker Class To Track Their BMI and Daily intakes
class DietTracker:
    def __init__(self,vegetables, fruits, grains, meats, dairy, bmi):
        self.daily_vegetables = vegetables
        self.daily_fruits = fruits
        self.daily_grains = grains
        self.daily_meats = meats
        self.daily_dairy = dairy
        self.bmi = bmi
    def validate(self):
        if not (0 < self.daily_vegetables <20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_fruits <20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_grains <20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_meats <20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_dairy <20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (5 < self.bmi <45):
            raise ValueError("Invalid Input Please Enter Again!")


#   User Input Function
def user_input():
    try:
        user_age = int(input("Enter your age: "))
        user_gender = input("Enter your gender (male or female only not Gmail :> ): ")
        user_weight = int(input("Enter your weight(kg): "))
        user_height = int(input("Enter your height(cm): "))

        user_vegetables = int(input("Enter your daily intake of vegetables:  "))
        user_fruits = int(input("Enter your daily intake of fruits: "))
        user_grains = int(input("Enter your daily intake of grains: "))
        user_meats = int(input("Enter your daily intake of meats: "))
        user_dairy = int(input("Enter your daily intake of dairy "))
        user_bmi = round(float(input("Enter your BMI: ")))
        return (Person(user_age, user_gender, user_weight, user_height),
                DietTracker(user_vegetables,user_fruits,user_grains,user_meats,user_dairy,user_bmi))

    except ValueError as e:(
        print(f"Error: {e}"))
    except Exception as e:(
        print(f"An unexpected error occurred: {e}"))

# Main Programs
    user_input();