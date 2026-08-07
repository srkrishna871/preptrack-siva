# preptrack-siva0

# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application that analyses a student’s placement-preparation performance. The application collects student details, attendance percentage, project completion status, profile verification status, and seven daily coding-practice scores.

The program validates user input, classifies performance for each practice day, calculates totals and averages, identifies the highest and lowest scores, detects the first critical score, evaluates placement readiness, and displays the first major blocker along with the next recommended action.

---

## Features Implemented

* Student profile input
* Student-name validation
* Attendance validation (0–100)
* Yes/No validation for project completion
* Yes/No validation for profile verification
* Seven-day practice score processing using a loop
* Practice-score validation
* Absent-day handling using `continue`
* Score classification:

  * Strong
  * Satisfactory
  * Needs Improvement
  * Critical
* Passed and failed day counting
* Strong, satisfactory, improvement, and critical day counting
* Highest-score detection
* Lowest-score detection
* First critical-score detection
* Total-score calculation
* Average-score calculation
* Division-by-zero prevention
* Placement-readiness evaluation
* Final status generation
* Primary blocker identification
* Next-action recommendation
* Final report display

---

## Python Concepts Used

* `print()`
* Variables
* Strings
* Integers
* Floating-point values
* Boolean values
* `input()`
* `int()`
* `float()`
* Arithmetic operators
* Relational operators
* Logical operators
* f-strings
* `if`
* `elif`
* `else`
* Compound conditions
* `while` loops
* `for` loops
* `range()`
* `continue`
* Counters
* Accumulators

---


## How to Run the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

If your system uses Python 3:

```bash
python3 main.py
```
---

## Sample Output

```text
==================================================
              PREPTRACK REPORT
==================================================
Student Name           : siva rama krishna.m
Registration Number    : 446
Graduation Year        : 2026
Attendance             : 85.0%

Attempted Days         : 7
Absent Days            : 0
Passed Days            : 7
Failed Days            : 0

Strong Days            : 5
Satisfactory Days      : 2
Needs Improvement Days : 0
Critical Days          : 0

Total Score            : 548
Average Score          : 78.29

Highest Score          : 90
Lowest Score           : 70

Final Status           : Ready for Mock Interview
Primary Blocker        : All criteria satisfied
Next Action            : Proceed to Mock Interview
==================================================
```

---



## Test Result Summary

| Test ID | Scenario                                         | Expected Result                 | Actual Result                           | Status |
| ------- | ------------------------------------------------ | ------------------------------- | --------------------------------------- | ------ |
| TC-01   | All requirements satisfied                       | Ready for Mock Interview        | Ready for Mock Interview                | Pass   |
| TC-02   | Critical score present                           | Critical Support Required       | Critical Support Required               | Pass   |
| TC-03   | Fewer than six attempts                          | Practice Incomplete             | Practice Incomplete                     | Pass   |
| TC-04   | Fewer than four passes                           | Insufficient Passed Practices   | Insufficient Passed Practices           | Pass   |
| TC-05   | Average below 70                                 | Practice Improvement Required   | Practice Improvement Required           | Pass   |
| TC-06   | Attendance below 75                              | Attendance Improvement Required | Attendance Improvement Required         | Pass   |
| TC-07   | Graduation year not eligible                     | Graduation Criteria Not Met     | Graduation Criteria Not Met             | Pass   |
| TC-08   | Project incomplete                               | Application On Hold             | Application On Hold                     | Pass   |
| TC-09   | Profile not verified                             | Application On Hold             | Application On Hold                     | Pass   |
| TC-10   | All days absent                                  | Practice Not Evaluated          | Practice Not Evaluated                  | Pass   |
| TC-11   | Invalid score below -1                           | Input rejected                  | Input rejected and prompted again       | Pass   |
| TC-12   | Invalid score above 100                          | Input rejected                  | Input rejected and prompted again       | Pass   |
| TC-13   | Boundary values (0, 39, 40, 59, 60, 74, 75, 100) | Correct classifications         | Correct classifications displayed       | Pass   |
| TC-14   | Multiple failed conditions                       | First major blocker displayed   | First major blocker displayed correctly | Pass   |

---

## Individual Contribution

* **Name:** siva rama krishna.m
* **Repository URL:** https://github.com/srkrishna871/preptrack-siva
* **My main contribution:** Implemented the complete execution flow in main.py — building input validation loops for all profile fields, constructing the seven-day practice analysis loop, tracking score metrics without any prohibited data structures, and establishing the priority-based final decision chain.
Checked team members repositories and explained their mistakes to modify and reviewed other's repositories and given feedback.
* **Features I implemented:** Input validation, score processing, score classification, counters, highest/lowest score logic, critical-score logic, average calculation, eligibility checks, final status logic, and final report display.
* **Python concepts I used:** Loops, conditions, Boolean expressions, counters, accumulators, and input validation.
* **Most difficult logic:** Determining the final status using the required priority order.
* **Problem I faced:** Correctly validating practice scores and handling absent days without affecting calculations.
* **How I solved it:** Used a validation loop for scores and `continue` for absent days so that calculations only used attempted scores.
---
## Code Review Completed

| Reviewed Member | Repository Link | What Was Done Well | Issue Identified | Suggested Improvement |
|---|---|---|---|---|
| sanketh | https://github.com/Saketh-ram-2004/preptrack-ksakethram | Good program structure, correct score processing, clear final report formatting, and proper use of loops and conditions | Input validation for attendance and project completion does not repeatedly ask until a valid value is entered | Use validation loops for attendance and project completion and improve invalid-input messages for better user experience |

## Feedback Received

**Reviewed By:** sanketh  

**Feedback Received:** Suggested improving the user experience by displaying clearer messages for invalid inputs and ensuring validation loops continue until a valid value is entered.

**Was the Feedback Valid?** Yes

**Change Made:** Reviewed and improved the validation flow for attendance and project-related inputs and updated the user prompts for better clarity.

**Commit Message Used:** `attendance validation changes`



## 📋 PrepTrack Submission Tracker

| # | Member Name        | GitHub Profile                              |          Repository                               | Status |
|---|-------------|----------------|------------|--------|
| 1 | K. Sanketh Ram     |  (https://github.com/Saketh-ram-2004)       |  (https://github.com/Saketh-ram-2004/ preptrack-ksakethram) | ✅ Completed |
| 2 | Harinadh           |  (https://github.com/Reddyharinadh)         |  (https://github.com/Reddyharinadh/preptrack-harinadh) | ✅ Completed |
| 3 | Puja Kumari        |  (https://github.com/Puja-hubb)             |  (https://github.com/Puja-hubb/Project1) | ✅ Completed |
| 4 | Karthik Kamuju     |  (https://github.com/karthikkamuju)         |  (https://github.com/karthikkamuju/preptrack-karthik) | ✅ Completed |
| 5 | Kareem Patan       |  (https://github.com/kareempatan)           |  (https://github.com/kareempatan/PrepTrack-Placement-Preparation-Performance-Analyzer) | ✅ Completed |
| 6 | S. Devi Prasad     |  (https://github.com/deviprasad-tech)       |  (https://github.com/deviprasad-tech/PrepTrack-Placement-Preparation-Performance-Analyzer) | ✅ Completed |
| 7 | Sandeep            |  (https://github.com/sandeep-9654)          |  (https://github.com/sandeep-9654/PrepTrack_Placement_Preparation_Performance_Analyzer) | ✅ Completed |
| 8 | Ganesh U           |  (https://github.com/GaneshUppananthala2005)|  (https://github.com/GaneshUppananthala2005/track_project-placement/tree/main) | ✅ Completed |
| 9 | Muhammed Ansil M A |  (https://github.com/MhdAnsil)              |  (https://github.com/MhdAnsil/preptrack-Ansil) | ✅ Completed |
| 10 | Karthik E         |  (https://github.com/karthik152-animal)     |  (https://github.com/karthik152-animal/preptrack-karthik) | ✅ Completed |
|11  |siva rama krishna.m|  (https://github.com/srkrishna871)          | (https://github.com/srkrishna871/preptrack-siva)           | ✅ Completed 