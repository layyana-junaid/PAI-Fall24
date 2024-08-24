#Layyana Junaid (23k-0056)
#calculate percentage and average for the dictionary data (input from the user)

subjects = {}

NumberSubjects = int(input("Enter the number of subjects: "))
for _ in range(NumberSubjects):
    subject = input("Enter the subject name: ")
    marks = int(input(f"Enter marks obtained in {subject}: "))
    subjects[subject] = marks

print("Dictionary containing subjects and marks value: ", subjects)

totalMarks = sum(subjects.values())
averageMarks = totalMarks / NumberSubjects

totalPossibleMarks = NumberSubjects * 100
percentage = (totalMarks / totalPossibleMarks) * 100

print("Average Marks:", averageMarks)
print("Percentage: ", percentage)

