class Person:
    def __init__(self, age, sex, height, weight, activity_level, goal_weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal_weight = goal_weight

    def calc_bmi(self): 
        return (self.weight * 703) / (self.height ** 2)

    def calc_bmr(self):
        weight_kg = self.weight / 2.205
        height_cm = self.height * 2.54

        if self.sex == "M": 
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * self.age) + 5
        else :
            return (10 * weight_kg) + (6.25 * height_cm) - (5 * self.age) - 161

    def calc_tdee(self):
        bmr = self.calc_bmr()

        if self.activity_level == "low":
            return bmr * 1.20
        elif self.activity_level == "medium":
            return bmr * 1.55
        elif self.activity_level == "high":
            return bmr * 1.725

    def calc_calories(self):
        tdee = self.calc_tdee()

        if self.goal_weight < self.weight: 
            return tdee - 500
        elif self.goal_weight == self.weight: 
            return tdee
        elif self.goal_weight > self.weight: 
            return tdee + 300

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
    sex = input("What is your sex (M/F)? ").upper().strip()
    while sex not in ("M" , "F"):
        sex = input("Please use M/F for your sex: ").upper().strip()

    # user input for height, with validation
    height = get_positive_number("What is your height? ")

    # user input for weight, with validation
    weight = get_positive_number("What is your weight? ")

    # user input for activity level, with validation
    activity_level = input("What is your activity level (low, medium, high)? ").lower().strip()
    while activity_level not in ("low" , "medium" , "high"):
        activity_level = input("Please enter a valid activity level (low, medium, or high): ").lower().strip()

    # user input for goal weight, with validation
    goal_weight = get_positive_number("What is your goal weight? ")

    # creates an instance of Person
    person1 = Person(age, sex, height, weight, activity_level, goal_weight)

    # prints the characters of the Person class
    print(f"Your BMI: {person1.calc_bmi():.2f}")
    print(f"Your BMR: {person1.calc_bmr():.2f}")
    print(f"Your TDEE: {person1.calc_tdee():.2f}")
    print(f"Your suggested caloric intake per day: {person1.calc_calories():.2f}")

if __name__ == "__main__":
    main()