import pandas as pd
import matplotlib.pyplot as plt
import csv

student_fields = ["ROLLNO", "NAME", "FATHER'SNAME", "MOTHER'SNAME", "PHONENO", "PHYSICS", "CHEMISTRY", "MATHEMATICS", "ENGLISH", "IP","LBS"]
student_database = 'students.csv'
student_database1 = 'UT1.csv'

def display_menu():
    print("\nStudent Database Management System\n")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Enter Roll no to see the graph")
    print("7. Quit")

def add_student():
    print("\nAdd Student Information\n")
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(student_data)

    print("Data saved successfully")
    input("Press any key to continue...")

def view_students():
    print("\n--- Student Records ---\n")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for field in student_fields:
            print(field.ljust(10), end="\t| ")
        print("\n" + "-" * 100)
        for row in reader:
            for item in row:
                print(item.ljust(10), end="\t| ")
            print("\n")
    input("Press any key to continue...")

def search_student():
    print("\n--- Search Student ---\n")
    roll = input("Enter roll no. to search: ")
    found = False
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and roll == row[0]:
                print("\n----- Student Found -----")
                for i in range(len(student_fields)):
                    print(f"{student_fields[i]}: {row[i]}")
                found = True
                break
    if not found:
        print("Roll No. not found in our database")
    input("Press any key to continue...")

def delete_student():
    print("\n--- Delete Student ---\n")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and roll != row[0]:
                updated_data.append(row)
            else:
                student_found = True

    if student_found:
        with open(student_database, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no.", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue...")

def update_student():
    print("\n--- Update Student ---\n")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if row and roll == row[0]:
                print(f"Student Found at index {idx}")
                student_data = []
                for field in student_fields:
                    value = input("Enter " + field + ": ")
                    student_data.append(value)
                updated_data.append(student_data)
                index_student = idx
            else:
                updated_data.append(row)

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student updated successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue...")

def graph():
    print("\n--- Student Marks Graph ---")
    roll = input("Enter roll no. to generate graph: ")
    found = False

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and roll == row[0]:
                student_name = row[1]
                found = True
                break

    if found:
        try:
            df = pd.read_csv(student_database1)
            student_row = df[df['ROLLNO'] == int(roll)]

            if student_row.empty:
                print("Marks not found for this student in UT1.csv")
            else:
                marks = student_row.iloc[0][['PHYSICS', 'CHEMISTRY', 'MATHEMATICS', 'ENGLISH', 'IP','LBS']]
                marks.plot(kind='bar', title=f"Marks of {student_name} (Roll: {roll})")
                plt.ylabel("Marks")
                plt.xlabel("Subjects")
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print("Error loading graph:", e)
    else:
        print("Roll No. not found in student database")

    input("Press any key to continue...")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        graph()
    elif choice == '7':
        print("\nThank you for using our system\n")
        break
    else:
        print("Invalid choice. Please try again.")
