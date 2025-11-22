a = int(input("Enter a: "))

len = a if a % 2 != 0 else a - 1

num = []

for i in range(1, len * 2, 2):
    num.append(i)
print(*num, sep=", ")

