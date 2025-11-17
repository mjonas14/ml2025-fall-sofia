import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Function for reading positive ints for N and k
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
    # Read N and k from user input
    N = read_pos_int("Enter number of data points (N): ")
    k = read_pos_int("Enter number of neighbors (k): ")

    # Initialie storage
    X_data = np.empty(N, dtype=float)
    Y_data = np.empty(N, dtype=float)

    print("\nEnter the data points (x, y):")
    for i in range(N):
        while True:
            try:
                x = float(input(f"  x{i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number for x.")

        while True:
            try:
                y = float(input(f"  y{i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number for y.")

        X_data[i] = x
        Y_data[i] = y

    label_variance = np.var(Y_data)
    print(f"\nVariance of labels in the training dataset: {label_variance:.4f}")

    # Check k against N
    if k > N:
        print("\nError: k must be less than or equal to N.")
        return

    # Prepare data for scikit-learn
    X_train = X_data.reshape(-1, 1)
    Y_train = Y_data

    # Initialize and train k-NN regressor using scikit-learn
    knn_regr = KNeighborsRegressor(n_neighbors=k)
    knn_regr.fit(X_train, Y_train)

    # Read test X value
    while True:
        try:
            X_test = float(input("\nEnter the X value for prediction: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number for X.")

    X_test_arr = np.array([[X_test]], dtype=float)
    Y_pred = knn_regr.predict(X_test_arr)[0]

    print(f"\nPredicted Y value (k-NN Regression): {Y_pred:.4f}")


# Call main function
if __name__ == "__main__":
    main()
