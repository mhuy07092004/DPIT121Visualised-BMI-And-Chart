import matplotlib.pyplot as plt

# Person Class Includes Their Information
class Person:
    # This class holds the user's personal information
    def __init__(self, age, gender, weight, height):
        self.age = age
        self.gender = gender.lower()
        self.weight = weight
        self.height = height

    def validate(self):
#         This method validates the user's personal information
        if not (0 < self.age < 120):
            raise ValueError("Invalid Age Please Enter Again!")
        if self.gender not in ["male", "female"]:
            raise ValueError("Invalid Gender Please Enter Again!")
        if not (20 < self.weight < 200):
            raise ValueError("Invalid Weight Please Enter Again!")
        if not (50 < self.height < 250):
            raise ValueError("Invalid Height Please Enter Again!")

# Tracker Class To Track Their BMI and Daily intakes
class DietTracker:
#     This class tracks the user's daily food intake and BMI
    def __init__(self, vegetables, fruits, grains, meats, dairy, bmi):
        self.daily_vegetables = vegetables
        self.daily_fruits = fruits
        self.daily_grains = grains
        self.daily_meats = meats
        self.daily_dairy = dairy
        self.bmi = bmi

    def validate(self):
#         This method validates the user's daily food intake
        if not (0 < self.daily_vegetables < 20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_fruits < 20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_grains < 20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_meats < 20):
            raise ValueError("Invalid Input Please Enter Again!")
        if not (0 < self.daily_dairy < 20):
            raise ValueError("Invalid Input Please Enter Again!")

# User Input Function
def user_input():
#     Gathers user input for personal and dietary information
    try:
        # User's basic in4 input
        user_age = int(input("Enter your age (in years): "))
        user_gender = str(input("Enter your gender (male or female): "))
        user_weight = float(input("Enter your weight (in kg): "))
        user_height = float(input("Enter your height (in cm): "))

        # User's intake input
        user_vegetables = float(input("Enter your daily intake of Vegetables (in servings): "))
        user_fruits = float(input("Enter your daily intake of Fruits (in servings): "))
        user_grains = float(input("Enter your daily intake of Grains (in servings): "))
        user_meats = float(input("Enter your daily intake of Meats (in servings): "))
        user_dairy = float(input("Enter your daily intake of Dairy (in servings): "))

        bmi = float(input("Your BMI is: "))
        return (Person(user_age, user_gender, user_weight, user_height),
                DietTracker(user_vegetables, user_fruits, user_grains, user_meats, user_dairy, bmi))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Visualization Functions
def create_bmi_chart(bmi, output_file):
#     This function creates a bar chart to visualize the user's BMI
    categories = ["Very Underweight", "Underweight", "Healthy Weight", "Overweight", "Obese"]
    y_positions = [6, 2, 6, 3, 2.5]  # Corresponding weight categories

    plt.figure(figsize=(10, 6))
    # Very underweight text
    plt.hlines(y=0, xmin=0, xmax=15, color="black", linestyles="solid")
    plt.text(7.5, 0, "Very Underweight", ha="center")
    # Underweight text
    plt.hlines(y=1, xmin=16, xmax=18, color="black", linestyles="solid")
    plt.text(17, 1, "Underweight", ha="center")
    # Healthy Weight Text
    plt.hlines(y=2, xmin=17, xmax=24, color="black", linestyles="solid")
    plt.text(20, 2, "Healthy Weight", ha="center")
    # Overweight Text
    plt.hlines(y=3, xmin=25, xmax=30, color="black", linestyles="solid")
    plt.text(27.5, 3, "Overweight", ha="center")
    # Obese text
    plt.hlines(y=4, xmin=30, xmax=35, color="black", linestyles="solid")
    plt.text(33, 4, "Obese", ha="center")
    # User BMI lines and text
    plt.vlines(x=bmi, ymin=6, ymax=-1, color="red", linestyles="solid")
    plt.text(x=bmi, y=5, s=f"Your BMI: {bmi:.2f}", ha="center", color="red")

    # Set chart limits
    plt.xlim(-2, 38)
    plt.ylim(6.5, -1.5)

    # Add labels and title
    plt.xlabel("BMI")
    plt.ylabel("Weight Category")
    plt.title("Bar Chart of BMI for Adults")

    # Save and close the plot
    plt.tight_layout()
    plt.savefig(output_file, format="jpg")
    plt.close()
    print(f"Plain Bar Chart saved as {output_file}")

def create_bar_chart(diet_tracker, output_file):
#     This function creates a bar chart to visualize the user's daily food intake
    categories = ["Vegetables", "Fruits", "Grains", "Meats", "Dairy"]
    recommended = [6, 2, 6, 3, 2.5]
    intake = [
        diet_tracker.daily_vegetables,
        diet_tracker.daily_fruits,
        diet_tracker.daily_grains,
        diet_tracker.daily_meats,
        diet_tracker.daily_dairy,
    ]

    x = range(len(categories))
    plt.figure(figsize=(10, 6))
    plt.bar(x, recommended, width=0.4, label="Recommended", color="orange", align="center")
    plt.bar([p + 0.4 for p in x], intake, width=0.4, label="Your Intake", color="blue", align="center")
    plt.xlabel("Food Group")
    plt.ylabel("Servings")
    plt.title("Daily Serving Intake")
    plt.xticks([p + 0.2 for p in x], categories)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, format="jpg")
    plt.close()
    print(f"Bar Chart saved as {output_file}")

def create_pie_chart(diet_tracker, output_file):
#     This function creates a pie chart to visualize the user's daily food intake
    categories = ["Vegetables", "Fruits", "Grains", "Meats", "Dairy"]
    recommended = [6, 2, 6, 3, 2.5]
    intake = [
        diet_tracker.daily_vegetables,
        diet_tracker.daily_fruits,
        diet_tracker.daily_grains,
        diet_tracker.daily_meats,
        diet_tracker.daily_dairy,
    ]

    colors = ["green", "orange", "blue", "red", "purple"]

    plt.figure(figsize=(12, 6))

    # User Intake Pie Chart
    plt.subplot(1, 2, 1)
    plt.pie(intake, labels=categories, autopct="%.1f%%", colors=colors)
    plt.title("User Intake")

    # Recommended Intake Pie Chart
    plt.subplot(1, 2, 2)
    plt.pie(recommended, labels=categories, autopct="%.1f%%", colors=colors)
    plt.title("Recommended Intake")

    plt.suptitle("Daily Serving Intake")
    plt.tight_layout()
    plt.savefig(output_file, format="jpg")
    plt.close()
    print(f"Pie Charts saved as {output_file}")

def create_bubble_chart(diet_tracker, output_file):
#    bubble chart to visualize the user's daily food intake
    categories = ["Vegetables", "Fruits", "Grains", "Meats", "Dairy"]
    recommended = [6, 2, 6, 3, 2.5]
    intake = [
        diet_tracker.daily_vegetables,
        diet_tracker.daily_fruits,
        diet_tracker.daily_grains,
        diet_tracker.daily_meats,
        diet_tracker.daily_dairy,
    ]

    plt.figure(figsize=(10, 6))
    plt.scatter(categories, recommended, s=[r * 40 for r in recommended], color="orange", alpha=0.5, label="Recommended Intake")
    plt.scatter(categories, intake, s=[i * 40 for i in intake], color="blue", alpha=0.5, label="User Intake")
    plt.xlabel("Food Group")
    plt.ylabel("Servings")
    plt.title("Daily Serving Intake")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, format="jpg")
    plt.close()
    print(f"Bubble Chart saved as {output_file}")

def create_line_chart(diet_tracker, output_file):
#     This function creates a line chart to visualize the user's daily food intake
    categories = ["Vegetables", "Fruits", "Grains", "Meats", "Dairy"]
    recommended = [6, 2, 6, 3, 2.5]
    intake = [
        diet_tracker.daily_vegetables,
        diet_tracker.daily_fruits,
        diet_tracker.daily_grains,
        diet_tracker.daily_meats,
        diet_tracker.daily_dairy,
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(categories, recommended, marker="o", label="Recommended", color="orange")
    plt.plot(categories, intake, marker="o", label="Intake", color="blue")
    plt.xlabel("Food Group")
    plt.ylabel("Servings")
    plt.title("Daily Serving Intake")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, format="jpg")
    plt.close()
    print(f"Line Chart saved as {output_file}")

# Export Data
def export_data(person, diet_tracker, file_name):
#     This function exports the user's personal and dietary information to a text file
    with open(file_name, "w") as file:
        file.write("User Information:\n")
        file.write(f"Age: {person.age}\n")
        file.write(f"Gender: {person.gender}\n")
        file.write(f"Weight: {person.weight} kg\n")
        file.write(f"Height: {person.height} cm\n")
        file.write("Daily Serving Intake:\n")
        file.write(f"Vegetables: {diet_tracker.daily_vegetables} servings\n")
        file.write(f"Fruits: {diet_tracker.daily_fruits} servings\n")
        file.write(f"Grains: {diet_tracker.daily_grains} servings\n")
        file.write(f"Meats: {diet_tracker.daily_meats} servings\n")
        file.write(f"Dairy: {diet_tracker.daily_dairy} servings\n")
    #The name of the text file to export the data to.
    print(f"Data has been exported to {file_name}")

# Main Program
if __name__ == "__main__":
    person, diet_tracker = user_input()
    # validate input
    if person and diet_tracker:
        person.validate()
        diet_tracker.validate()

        # Ask if the user wants to save the BMI chart
        if input("Would you like to save the BMI chart? (yes/no): ").lower() == "yes":
            create_bmi_chart(diet_tracker.bmi, "visualize_bmi_chart.jpg")

        # Ask if the user wants to save the charts
        if input("Would you like to save the charts? (yes/no): ").lower() == "yes":
            create_bar_chart(diet_tracker, "visualize_bar_chart_chart.jpg")
            create_pie_chart(diet_tracker, "visualize_pie_charts_chart.jpg")
            create_bubble_chart(diet_tracker, "visualize_bubble_chart_chart.jpg")
            create_line_chart(diet_tracker, "visualize_line_chart_chart.jpg")

        # Ask if the user wants to export the data
        if input("Do you also want to export your data? (yes/no): ").lower() == "yes":
            export_data(person, diet_tracker, "user_info.txt")
