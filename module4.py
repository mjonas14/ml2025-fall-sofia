# Program that finds the index of a number in a list of N numbers
# If it cant be found, it returns the index -1

# Read N from user
inp = input("How many numbers do you want to input?: ")
N = int(inp)

# Read N numbers one at a time
numbers = []
print("Now please input the numbers:")
for i in range(N):
    num = int(input())
    numbers.append(num)

print("Now please input the number you want to find:")
# Read integer to search for
X = int(input())

print("Calculating index...")
# Find index of number X, if it exists
index = -1
for i in range(N):
    if numbers[i] == X:
        index = i + 1 # Converting so that it starts at index 1
        break

print(index)