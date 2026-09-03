class Person:
    def __init__(self, age, sex, height, weight, activity_level, goal_weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal_weight = goal_weight

    # calculates BMI
    def calc_bmi(self): 
        return (self.weight * 703) / (self.height ** 2)

    # calculates BMR - Basal Metabolic Rate
    def calc_bmr(self):
        weight_kg = self.weight / 2.205
        height_cm = self.height * 2.54

        if self.sex == "M": 
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * self.age) + 5
        else :
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * self.age) - 161

    # calculates TDEE - Total Daily Energy Expenditure
    def calc_tdee(self):
        bmr = self.calc_bmr()

        if self.activity_level == "low":
            return bmr * 1.20
        elif self.activity_level == "medium":
            return bmr * 1.55
        elif self.activity_level == "high":
            return bmr * 1.725

    # calculates suggested caloric intake
    def calc_calories(self):
        tdee = self.calc_tdee()

        if self.goal_weight < self.weight: 
            return tdee - 500
        elif self.goal_weight == self.weight: 
            return tdee
        elif self.goal_weight > self.weight: 
            return tdee + 300

    # calculates suggested protein intake
    def calc_protein(self):
        return self.goal_weight

    # calculates suggested fat intake
    def calc_fat(self):
        return (self.calc_calories() * 0.25) / 9

    # calculates suggested carb intake
    def calc_carbs(self):
        return (self.calc_calories() - ((self.calc_protein() * 4) + (self.calc_fat() * 9))) / 4


# out of the class

def get_positive_number(prompt, maximum=None):

    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                print("Please enter a number greater than 0.")
            elif maximum is not None and number > maximum:
                print(f"Please enter a number no greater than {maximum}.")
            else:
                return number

        except ValueError:
            print("Please enter a number.")


def main():

    # User input for age, with validation 
    age = get_positive_number("What is your age? ", 100)

    # user input for sex, with validation
    sex = input("What is your sex (M/F)? ").strip().upper()
    while sex not in ("M" , "F"):
        sex = input("Please use M/F for your sex: ").strip().upper()

    # user input for height, with validation
    height = get_positive_number("What is your height (in inches)? ")

    # user input for weight, with validation
    weight = get_positive_number("What is your weight (in pounds)? ")

    # user input for activity level, with validation
    activity_level = input("What is your activity level (low, medium, high)? ").strip().lower()
    while activity_level not in ("low" , "medium" , "high"):
        activity_level = input("Please enter a valid activity level (low, medium, or high): ").strip().lower()

    # user input for goal weight, with validation
    goal_weight = get_positive_number("What is your goal weight (in pounds)? ")

    # creates an instance of Person
    person1 = Person(age, sex, height, weight, activity_level, goal_weight)

    # prints the characters of the Person class
    print("=======================")
    print("==== NUTRITION LOG ====")
    print("=======================")
    print("YOUR INFORMATION: ")
    print("------------------")
    print(f"Age: {person1.age:.0f} years old")
    print("Sex: " + str(person1.sex))
    print("Height: " + str(person1.height)+ " inches")
    print("Weight: " + str(person1.weight) + " lbs")
    print("Activity Level: " + str(person1.activity_level))
    print("Goal Weight: " + str(person1.goal_weight) + " lbs")

    print("")
    print("NUTRITION ESTIMATES: ")
    print("------------------")
    print(f"BMI: {person1.calc_bmi():.2f}")
    print(f"BMR: {person1.calc_bmr():.2f} calories")
    print(f"TDEE: {person1.calc_tdee():.2f} calories")
    print(f"Suggested caloric intake per day: {person1.calc_calories():.0f} calories")

    print("")
    print("MACRONUTRIENT ESTIMATES: ")
    print("------------------")
    print(f"Suggested protein intake per day: {person1.calc_protein():.0f} grams")
    print(f"Suggested fat intake per day: {person1.calc_fat():.0f} grams")
    print(f"Suggested carbohydrate intake per day: {person1.calc_carbs():.0f} grams")



if __name__ == "__main__":
    main()