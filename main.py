# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TOD0: Validate that the student name is not empty.
student_name = input("Enter student name: ")
while student_name == "":
    print("Student name should not be empty.")
    student_name = input("Enter student name: ")

registration_number = input("Enter registration number: ")


graduation_year = int(input("Enter graduation year: "))

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

if graduation_eligible:
    print("Eligible for placement.")
else:
    print("Not eligible for placement.")

# TODo: Validate attendance between 0 and 100.
attendance = float(input("Enter attendance percentage: "))
while attendance < 0 or attendance > 100:
    print("Enter valid attandance between 0 and 100!")
    attendance = float(input("Enter attendance percentage: "))

# TODo: Accept only yes or no.
project_input = input(
    "Has the student completed the required project? Enter yes or no: "
)
while not (project_input == "yes" or project_input == "no"):
    print("Invalid input! Enter yes or no")
    project_input = input(
        "Has the student completed the required project? Enter yes or no: "
    )

 