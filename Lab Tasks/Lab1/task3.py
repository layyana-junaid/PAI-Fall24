
Lists = []
for i in range (0, 5, 1):
  l = int(input("Enter Integer: "))
  Lists.append(l)
print(Lists)

count = 0
for i in range (0, 5):
  if Lists[i] % 2 == 0:
    count = count + 1
print(count)
