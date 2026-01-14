students = []

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
    
#function to add a new student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks (out of 100): "))
    grade = calculate_grade(marks)
    students.append({"name": name, "roll": roll, "marks": marks, "grade": grade})
    print("Student record added successfully!\n")


#function to view all student
def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Name: {student['name']}, Roll No: {student['roll']}, Marks: {student['marks']}, Grade: {student['grade']}")
    print()

def main():
    while True:
        print("=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()