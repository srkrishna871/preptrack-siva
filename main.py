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

if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# TODo: Accept only yes or no.
profile_input = input(
    "Is the student profile verified? Enter yes or no: "
)
while not (profile_input == "yes" or profile_input == "no"):
    print("Invalid input! Enter yes or no: ")
    profile_input = input(
        "Is the student profile verified? Enter yes or no: "
    )

#TODo: Convert profile_input into True or False.
profile_verified = False
if profile_input == "yes":
    profile_verified = True

# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

#--------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    # TODO: Use a while loop to accept only:
    # -1 or a score between 0 and 100.
    score = int(
        input(
            f"Enter Day {day} score from 0 to 100, "
            "or -1 for absent: "
        )
    )
    while score != -1 and (score < 0 or score > 100):
        score = int(
            input(
                f"Invalid input! Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )

    # TODO: Handle absence.
    # Increase absent_days and use continue.
    if score == -1:
        absent_days += 1
        continue

    # TODO: Increase attempted_days and total_score.
    else:
        attempted_days += 1
        total_score += score

    # TODO: Initialize or update:
    # highest_score, highest_score_day,
    # lowest_score and lowest_score_day.
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day
        lowest_score = score
        lowest_score_day = day
        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day
        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # TODO: Classify the score:
    # 75–100  -> Strong 
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical
    if score >= 75:
        strong_days += 1
    elif score >= 60:
        satisfactory_days += 1
    elif score >= 40:
        improvement_days += 1
    else:
        critical_days += 1

    # TODO: Count passed and failed days.
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

    # TODO: Store only the first critical day and score.
    if score < 40 and not critical_score_found:
        critical_score_found = True
        first_critical_day = day
        first_critical_score = score


#4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODo: Prevent division by zero.
average_score = 0
if attempted_days > 0:
    average_score = total_score / attempted_days

 