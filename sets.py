def sets(prompt):
    return set(map(int, input(prompt).split()))

set1 = sets("Enter the first set elements here: ")
set2 = sets("Enter the second set elements here: ")

bothsets = set1.intersection(set2)
print("First set:", set1)
print("second set:", set2)
print("bothsets:", bothsets)