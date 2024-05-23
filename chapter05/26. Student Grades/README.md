# Filtering Students by Average Grade in Python

This script filters a list of students based on their average grades. It uses dictionary comprehension to create a new dictionary containing only the students whose average grade exceeds a user-defined threshold.

## Script Overview 📘

The script defines a dictionary of students and their grades, calculates the average grade for each student, and filters out students whose average grade is below a specified threshold. The results are displayed with the average grades rounded to two decimal places.

### :computer: Script Code

```python
# List of students and their grades
students = {
    'Alice': [85, 92, 78],      # 85.00
    'Bob': [79, 95, 88],        # 87.33
    'Charlie': [68, 72, 80],    # 73.33
    'Diana': [95, 98, 100],     # 97.67
    'Eve': [50, 60, 58]         # 56.00
}

def main():
    # Threshold for average grade
    threshold = int(input("Please insert the threshold (integer): "))

    # Using dictionary comprehension to create a dictionary of students and their average grades
    # Only include students whose average grade is above the threshold
    # Average grade with 2 decimals
    average_grades = {student: round(sum(grades) / len(grades), 2) for student, grades in students.items() if sum(grades) / len(grades) > threshold}

    print(f"\nStudents with average grade greater than {threshold}:")
    # Output the result using a for loop
    for student, avg_grade in average_grades.items():
        print(f"{student}: {avg_grade:.2f}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Dictionary Comprehension**: Learn how to create dictionaries using dictionary comprehensions in Python.
- **Filtering by Condition**: Understand how to filter elements within a dictionary comprehension based on a condition.
- **Average Grade Calculation**: See how to calculate the average grade for each student and round it to two decimal places.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `26_student_grades.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `26_student_grades.py`.
5. Run the script with: `python 26_student_grades.py`.

## Usage Example 📋
Execute the script and input an integer threshold to see which students have an average grade above that threshold. The script will print the names and average grades of the qualifying students.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
