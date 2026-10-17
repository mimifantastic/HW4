# Collect the student's name and three exam scores.
name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

if not (0 <= exam1 <= 100 and 0 <= exam2 <= 100 and 0 <= exam3 <= 100):
    print("Each exam score must be between 0 and 100.")
else:
    average = (exam1 + exam2 + exam3) / 3

    # Check cutoffs from highest to lowest. Use the unrounded average;
    # for example, 89.5 earns A-, while 90 earns A.
    if average >= 90:
        grade = "A"
    elif average >= 87:
        grade = "A-"
    elif average >= 83:
        grade = "B+"
    elif average >= 80:
        grade = "B"
    elif average >= 77:
        grade = "B-"
    elif average >= 73:
        grade = "C+"
    elif average >= 70:
        grade = "C"
    elif average >= 67:
        grade = "C-"
    elif average >= 63:
        grade = "D+"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Standing has its own thresholds, also checked highest first.
    if average >= 90:
        status = "Dean's List"
    elif average >= 70:
        status = "Good Standing"
    elif average >= 60:
        status = "Academic Probation"
    else:
        status = "Academic Suspension Warning"

    print("\n============================")
    print("    STUDENT GRADE REPORT")
    print("============================")
    print(f"Student: {name}")
    print(f"Exam 1:  {exam1:g}")
    print(f"Exam 2:  {exam2:g}")
    print(f"Exam 3:  {exam3:g}")
    print("----------------------------")
    print(f"Average: {average:.2f}")
    print(f"Grade:   {grade}")
    print(f"Status:  {status}")
    print("============================")
