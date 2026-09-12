terms = int(input("Enter the number of terms: "))

first, second = 0, 1
for _ in range(terms):
	print(first, end=" ")
	first, second = second, first + second

print()
