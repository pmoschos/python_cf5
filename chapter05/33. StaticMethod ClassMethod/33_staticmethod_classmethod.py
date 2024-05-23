# @classmethod:

# First argument is cls, which refers to the class.
# Can access and modify class-level data.
# Useful for factory methods and class-level operations.

# @staticmethod:

# No implicit first argument (self or cls).
# Cannot access or modify class or instance data.
# Useful for utility functions related to the class.
    
class Employee:
    _total_employees = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee._total_employees += 1

    @classmethod
    def total_employees(cls):
        """
        Class method to get the total number of employees created.
        """
        return cls._total_employees

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        """
        Static method to calculate the annual bonus based on salary and bonus percentage.
        """
        return salary * (bonus_percentage / 100)

    @classmethod
    def incorrect_class_method(cls):
        """
        Incorrectly tries to access instance-level attributes.
        """
        try:
            print(cls.first_name)  # This will cause an AttributeError
        except AttributeError as e:
            print(f"Error in class method: {e}")

    @staticmethod
    def incorrect_static_method():
        """
        Incorrectly tries to access class-level attributes.
        """
        try:
            print(Employee._total_employees)  # This will actually work since we access class-level attribute directly
        except AttributeError as e:
            print(f"Error in static method: {e}")

def main():
    # Creating employee instances
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Jane", "Smith", 60000)

    # Getting the total number of employees created
    total_emps = Employee.total_employees()
    print(f"Total employees created: {total_emps}")  # Output: Total employees created: 2

    # Calculating annual bonus
    bonus = Employee.calculate_bonus(emp1.salary, 10)
    print(f"Annual bonus for {emp1.first_name} {emp1.last_name}: {bonus}")  # Output: Annual bonus for John Doe: 5000.0

    bonus = Employee.calculate_bonus(emp2.salary, 15)
    print(f"Annual bonus for {emp2.first_name} {emp2.last_name}: {bonus}")  # Output: Annual bonus for Jane Smith: 9000.0

    # Demonstrating incorrect usage
    print("\nDemonstrating incorrect usages:")

    # Incorrect class method usage
    Employee.incorrect_class_method()  # This will raise an AttributeError

    # Incorrect static method usage
    Employee.incorrect_static_method()  # This will not raise an error but is shown for demonstration

if __name__ == "__main__":
    main()
