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

    print(f"\nStudents with average grade grater than {threshold}:")
    # Output the result using a for loop
    for student, avg_grade in average_grades.items():
        print(f"{student}: {avg_grade:.2f}")
        # print(f"{student}: {avg_grade:.2f}")


if __name__ == "__main__":
    main()