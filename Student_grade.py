def student_grades_manager():
    """
    Manages a dictionary of student grades by allowing the user to add, update, and print grades.
    """
    grades = {}

    while True:
        # Display menu options to the user
        print("\nStudent Grades Manager")
        print("1. Add a new student and grade")
        print("2. Update an existing student's grade")
        print("3. Print all student grades")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new student and grade
            name = input("Enter the student's name: ")
            grade = input(f"Enter the grade for {name}: ")
            grades[name] = grade
            print(f"Added {name} with grade {grade}.")

        elif choice == '2':
            # Update an existing student's grade
            name = input("Enter the name of the student to update: ")
            if name in grades:
                new_grade = input(f"Enter the new grade for {name}: ")
                grades[name] = new_grade
                print(f"Updated {name}'s grade to {new_grade}.")
            else:
                print(f"Error: Student '{name}' not found.")

        elif choice == '3':
            # Print all student grades
            if not grades:
                print("No grades have been entered yet.")
            else:
                print("\n--- Current Student Grades ---")
                for name, grade in grades.items():
                    print(f"{name}: {grade}")

        elif choice == '4':
            # Quit the program
            print("Exiting program.")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the grades manager
student_grades_manager()
