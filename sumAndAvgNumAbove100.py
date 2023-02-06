# Prints the sum and average of the numbers above 100

oldList=[74,19,105,20,-2,67,77,124,-45,38]
newList=[new for new in oldList if 0<=new<=100]
print(sum(newList),sum(newList)/len(newList))
