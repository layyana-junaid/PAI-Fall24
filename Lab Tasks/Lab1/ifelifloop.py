#marks department system

marks = int(input("Enter your marks: "))

if marks >= 80:
  print("you are enrolled in CS department")
  if marks > 85:
    print("CS-A is your section")
  else: print("CS-B is your section")

elif marks >= 70:
  print("you are enrolled in AI department")
  if marks > 75:
    print("AI-A is your section")
  else: print("AI-B is your section")

elif marks >= 60:
  print("you are enrolled in DS department")
  if marks > 65:
    print("DS-A is your section")
  else: print("DS-B is your section")
