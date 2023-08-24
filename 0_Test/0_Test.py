arr = [1, 2, 3]
subsets = [[]]

for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
print(subsets)