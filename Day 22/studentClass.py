class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Create two student objects
student1 = Student("Alice", 18)
student2 = Student("Bob", 20)

# Add grades for student1
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

# Add grades for student2
student2.add_grade(90)
student2.add_grade(88)
student2.add_grade(95)

# Calculate and print the average grades for each student
average_grade1 = student1.get_average_grade()
average_grade2 = student2.get_average_grade()

print(f"{student1.name}'s average grade:", average_grade1)
print(f"{student2.name}'s average grade:", average_grade2)
