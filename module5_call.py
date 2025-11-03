from module5_mod import NumList

def main():
    # Read N from user
    while True: 
        try:
            inp = input("How many numbers do you want to input?: ")
            N = int(inp)
            if N > 0:
                break
            else:
                print("N must be a positive integer! Please try again.")
        except ValueError: 
            print("Invalid input, please enter a positive integer")

    # Read N numbers one at a time
    nums = NumList()
    
    print("Now please input the numbers:")
    for i in range(N):
        num = int(input())
        nums.insert_number(num)

    print("Now please input the number you want to find:")
    # Read integer to search for
    X = int(input())

    print("Calculating index...")
    # Find index of number X, if it exists
    print(nums.find_number(X))

if __name__ == "__main__":
    main()