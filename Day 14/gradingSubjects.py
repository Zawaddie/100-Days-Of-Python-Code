def calculateGrade(score):
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

def findSum(arr):
    curr =0
    for val in arr:
        curr += val
    return curr

def calculateOverallGrade(grades):
    overall_mean = findSum(grades) / len(grades)
    overall_grade = calculateGrade(overall_mean)
    return overall_mean, overall_grade


def validate_score(score):
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        return False
    return True


subjects = ['Maths', 'English', 'Kiswahili', 'Science', 'Geography']
grades = []

for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter the score for {subject}: "))
            if validate_score(score):
                grades.append(score)
                break
            # grade = calculateGrade(score)
            # print(f"{subject}: {grade}")
        except:
            print("Only Integer are required")


overall_mean, overall_grade = calculateOverallGrade(grades)
total_marks = findSum(grades)


#print(f"\nScores in summary: {subjects}{grades}")
sorted_scores = sorted(grades)
#print("Sorted Scores:", sorted_scores)

print("\n\tHey Zawadi, Here is summary of your score:\n")
print("SUBJECT \tSCORE  \tGRADE")
for score in sorted_scores:
    subject = subjects[grades.index(score)]
    print(f"{subject} \t{score} \t{calculateGrade(score)}")
print(f"Overall   \t{overall_mean}\t{overall_grade}")
print(f"Total Marks: {total_marks}")