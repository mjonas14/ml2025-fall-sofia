import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import accuracy_score


def read_pos_ints(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_non_neg_ints(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def read_data_points(num: int, set_name: str) -> tuple[np.ndarray, np.ndarray]:
    X_data = np.empty(num, dtype=float)
    Y_data = np.empty(num, dtype=int)

    print(f"\nEnter the {set_name} data points (x, y):")
    print("(x = input feature, y = class label)")
    for i in range(num):
        while True:
            try:
                x = float(input(f"  x{i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number for x.")

        while True:
            try:
                y = read_non_neg_ints(f"  y{i + 1}: ")
                break
            except ValueError:
                print("Invalid input. Please enter a non-negative integer for y.")

        X_data[i] = x
        Y_data[i] = y

    return X_data, Y_data


def main() -> None:
    # Read N and training set
    N = read_pos_ints("Enter number of training data points (N): ")
    X_train, y_train = read_data_points(N, "training")

    # Read M and test set
    M = read_pos_ints("\nEnter number of test data points (M): ")
    X_test, y_test = read_data_points(M, "test")

    X_train_2d = X_train.reshape(-1, 1)
    X_test_2d = X_test.reshape(-1, 1)

    # Using KFold to avoid stratification issues
    cv_folds = 3 if N >= 6 else 2
    cv = KFold(n_splits=cv_folds, shuffle=False)
    
    min_train_size = N * (cv_folds - 1) // cv_folds
    max_k = min(10, min_train_size)
    
    param_grid = {'n_neighbors': list(range(1, max_k + 1))}

    knn_classifier = KNeighborsClassifier()
    
    grid_search = GridSearchCV(
        knn_classifier,
        param_grid,
        scoring='accuracy',
        cv=cv,
        return_train_score=False
    )

    grid_search.fit(X_train_2d, y_train)
    
    best_k = grid_search.best_params_['n_neighbors']

    best_classifier = KNeighborsClassifier(n_neighbors=best_k)
    best_classifier.fit(X_train_2d, y_train)

    # Predict on test set
    y_pred = best_classifier.predict(X_test_2d)

    # Calculate test accuracy
    test_accuracy = accuracy_score(y_test, y_pred)

    print(f"\nBest k: {best_k}")
    print(f"Test accuracy: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()
