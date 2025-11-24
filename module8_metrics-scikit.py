import numpy as np
from sklearn.metrics import precision_score, recall_score

# Function for reading positive ints for N
def read_pos_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def main() -> None:
    # Read N from user input
    N = read_pos_int("Enter number of data points (N): ")

    X_vals = np.empty(N, dtype=int)
    Y_vals = np.empty(N, dtype=int)

    print("\nEnter the data points (x, y):")
    print("(x = ground truth, y = predicted, must be 0 or 1)")
    for i in range(N):
        while True:
            try:
                x = int(input(f"  x{i + 1}: "))
                if x != 0 and x != 1:
                    print("Invalid input. Please enter 0 or 1 for x.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter 0 or 1 for x.")

        while True:
            try:
                y = int(input(f"  y{i + 1}: "))
                if y != 0 and y != 1:
                    print("Invalid input. Please enter 0 or 1 for y.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter 0 or 1 for y.")

        X_vals[i] = x
        Y_vals[i] = y

    # Compute Precision and Recall using scikit-learn
    precision = precision_score(X_vals, Y_vals, zero_division=0)
    recall = recall_score(X_vals, Y_vals, zero_division=0)

    print(f"\nPrecision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

# Call main function
if __name__ == "__main__":
    main()
