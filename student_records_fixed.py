# =============================================================================
# Student Record Management System
# Programming Fundamentals with Python - Week 8 Refactoring Exercise
#
# This program reads student data from a CSV file and provides a menu-driven
# interface to list all students and search for a student by ID.
#
# NOTE TO STUDENTS: This program works correctly but is written in a "top-down"
# style with no functions and uses global variables. Your task is to refactor
# this program to make it more readable and maintainable by organizing the code
# into well-named functions and eliminating the use of global variables.
# =============================================================================

import csv

def read_csv(filename):
    student_records = []

    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            student_records.append(row)

    return student_records

def list_students(student_records):
    if not student_records:
        print("No student records available.")
        return

    print()
    print("-" * 82)
    print(f"{'#':<5} {'Student ID':<12} {'Student Name':<22} {'Major':<24} {'GPA':<6} {'Credits'}")
    print("-" * 82)

    for row_number, student in enumerate(student_records, start=1):
        print(
            f"{row_number:<5}"
            f"{student['StudentID']:<12}"
            f"{student['StudentName']:<22}"
            f"{student['Major']:<24}"
            f"{student['GPA']:<6}"
            f"{student['TotalCredits']}"
        )

    print("-" * 82)
    print(f"Total records: {len(student_records)}")

def binary_search(student_records, search_id):
    sorted_students = sorted(
        student_records,
        key=lambda student: student["StudentID"].strip().upper()
    )

    low = 0
    high = len(sorted_students) - 1
    search_id = search_id.strip().upper()

    while low <= high:
        middle = (low + high) // 2
        middle_id = sorted_students[middle]["StudentID"].strip().upper()

        if middle_id == search_id:
            return sorted_students[middle]
        elif middle_id < search_id:
            low = middle + 1
        else:
            high = middle - 1

    return None    

def main():
    student_records = []
    csv_loaded = False
    csv_filename = ""

    print("=" * 60)
    print("    Student Record Management System")
    print("=" * 60)

    while True:
        print()
        print("Please select an option:")
        print("  1. Read CSV")
        print("  2. List CSV Contents")
        print("  3. Search for Student by ID")
        print("  4. Exit")
        print()

        menu_choice = input("Enter your choice (1-4): ").strip()

        # =========================================================================
        # Option 1: Read CSV
        # =========================================================================
        if menu_choice == "1":
            csv_filename = input("Enter the CSV filename (e.g., students.csv): ").strip()
            student_records = read_csv(csv_filename)
            csv_loaded = True

            print()
            print(f"Success! {len(student_records)} student record(s) loaded from '{csv_filename}'.")

        # =========================================================================
        # Option 2: List CSV Contents
        # =========================================================================
        elif menu_choice == "2":
            if not csv_loaded:
                print()
                print("No data loaded. Please use Option 1 to read a CSV file first.")
            else:
                list_students(student_records)

        # =========================================================================
        # Option 3: Search for Student by ID
        # =========================================================================
        elif menu_choice == "3":
            if not csv_loaded:
                print()
                print("No data loaded. Please use Option 1 to read a CSV file first.")
            else:
                search_id = input("Enter the Student ID to search for: ").strip()
                found_student = binary_search(student_records, search_id)

                print()

                if found_student is None:
                    print(f"No student found with ID '{search_id}'.")
                else:
                    print("Student found!")
                    print("-" * 40)
                    print(f"  Student ID    : {found_student['StudentID']}")
                    print(f"  Student Name  : {found_student['StudentName']}")
                    print(f"  Major         : {found_student['Major']}")
                    print(f"  GPA           : {found_student['GPA']}")
                    print(f"  Total Credits : {found_student['TotalCredits']}")
                    print("-" * 40)

        # =========================================================================
        # Option 4: Exit
        # =========================================================================
        elif menu_choice == "4":
            print()
            print("Thank you for using the Student Record Management System. Goodbye!")
            break

        # =========================================================================
        # Invalid Input
        # =========================================================================
        else:
            print()
            print(f"'{menu_choice}' is not a valid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
