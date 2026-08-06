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

# TODO: Validate that the student name is not empty.
student_name = input("Enter student name: ")
while student_name == "":
    print("Student name should not be empty.")
    student_name = input("Enter student name: ")

registration_number = input("Enter registration number: ")
 