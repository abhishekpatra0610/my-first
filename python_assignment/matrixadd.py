rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = []
print("Enter elements of First Matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"A[{i}][{j}] = "))
        row.append(element)
    A.append(row)


B = []
print("Enter elements of Second Matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"B[{i}][{j}] = "))
        row.append(element)
    B.append(row)

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)


print("\nResultant Matrix:")
for row in result:
    print(row)