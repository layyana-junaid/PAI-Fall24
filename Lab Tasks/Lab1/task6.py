#Layyana Junaid (23k-0056)
#taking input from user and storing them in dictionary
subDict = {}

NumberSub = int(input("Enter the number of subjects you want to add: "))

for _ in range(NumberSub):
    subject = input("Subjects Name: ")
    marks = int(input("Marks Obtained: "))
    subDict[subject] = marks
    
print("Dictionary containing subjects and marks value: ", subDict)

totalMarks = sum(subDict.values())
NumberSub = len(subDict)
averageMarks = total_marks / NumberSub

print("Average Marks:", averageMarks)

# Find the subject with the highest marks
highestSubject = max(subDict, key=subDict.get)
highestMarks = subDict[highestSubject]


print("Subject with Highest Marks:", highestSubject)
print("Marks in", highestSubject + ":", highestMarks)