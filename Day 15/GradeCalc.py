test_scores = (75, 82, 88, 92, 79)
print("Test Scores:", test_scores)


average_score = sum(test_scores) / len(test_scores)
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the average score and grade
print("Average Score:", average_score)
print("Grade:", grade)
