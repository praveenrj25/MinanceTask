n = int(input("Enter number of elements: "))
numList = []

print("Enter the values")
for i in range(n):
    numList.append(int(input()))

print(numList)

numList = [x for x in numList if x % 2 != 0]
print(numList)
