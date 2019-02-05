# Iterate a given list and check if a given element already exists in a
# dictionary as a key’s value, if not delete it from the list.

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print(rollNumber)

# Expected Outcome after removing unwanted elements from list [47, 69, 76, 97]
