a = int(input("Enter a: "))


limit = a if a % 2 != 0 else a - 1

result = []


for i in range(1, limit * 2, 2):
    result.append(i)

print(*result, sep=", ")
