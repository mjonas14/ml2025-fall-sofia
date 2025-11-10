import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.Y_train = None

    def train(self, X, y):
        self.X_train = np.array(X, dtype=float)
        self.Y_train = np.array(y, dtype=float)

    def predict(self, X_test):
        if self.k > len(self.X_train):
            raise ValueError("k cannot be greater than N!")

        # Compute distances
        distances = np.abs(self.X_train - X_test)

        # Get the indices of the k nearest neighbors
        nn_indices = np.argsort(distances)[:self.k]

        # Compute the mean Y value of the nearest neighbors
        y_pred = np.mean(self.Y_train[nn_indices])
        return y_pred


def main():
    N = int(input("Enter number of data points (N): "))
    k = int(input("Enter number of neighbors (k): "))

    X_data = []
    Y_data = []
    print("\nEnter the data points:")
    for i in range(N):
        x = float(input(f"  x{i+1}: "))
        X_data.append(x)
        y = float(input(f"  y{i+1}: "))
        Y_data.append(y)

    X_test = float(input("\nEnter the X value for prediction: "))

    knnModel = KNN(k)
    knnModel.train(X_data, Y_data)

    try:
        y_pred = knnModel.predict(X_test)
        print(f"\nPredicted Y value: {y_pred:.1f}")
    except ValueError as e:
        print("\n", e)


if __name__ == "__main__":
    main()
