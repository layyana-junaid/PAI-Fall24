Lists = []
for i in range (0, 5, 1):
  l = int(input("Enter Integer: "))
  Lists.append(l)
print(Lists)

sum = 0
for i in range (0, 5):
  sum = sum + Lists[i]
print(sum)
