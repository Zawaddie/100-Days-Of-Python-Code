def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def calculate_overall_grade(grades):
    overall_mean = sum(grades) / len(grades)
    overall_grade = calculate_grade(overall_mean)
    return overall_mean, overall_grade


def validate_score(score):
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        return False
    return True


subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']
grades = []

for subject in subjects:
    while True:
        score = float(input(f"Enter the score for {subject}: "))
        if validate_score(score):
            break
    grade = calculate_grade(score)
    grades.append(score)
    print(f"{subject}: {grade}")

overall_mean, overall_grade = calculate_overall_grade(grades)
total_marks = sum(grades)

print(f"\nOverall Mean: {overall_mean}")
print(f"Overall Grade: {overall_grade}")
print(f"Total Marks: {total_marks}")
