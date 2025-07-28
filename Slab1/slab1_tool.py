import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def data_analysis():
    print("\n🔍 CSV Data Analysis and Visualization")
    try:
        file_path = input("price.csv")
        df = pd.read_csv(file_path)
        print("\nFirst 5 rows:\n", df.head())

        column = input("\nEnter column name to calculate average: ")
        if column in df.columns:
            print(f"Average of '{column}':", df[column].mean())
        else:
            print("Column not found.")

        print("\nGenerating visualizations...")

        # Bar chart (value count of a categorical column)
        cat_col = input("Enter column name for bar chart (categorical): ")
        if cat_col in df.columns:
            df[cat_col].value_counts().plot(kind='bar', title=f'Bar Chart of {cat_col}')
            plt.show()

        # Scatter Plot
        x_col = input("Enter X-axis column for scatter plot: ")
        y_col = input("Enter Y-axis column for scatter plot: ")
        if x_col in df.columns and y_col in df.columns:
            plt.scatter(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Scatter Plot")
            plt.show()

        # Heatmap
        print("\nCorrelation Heatmap:")
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.show()

    except Exception as e:
        print("Error:", e)


def linear_regression():
    print("\n🏠 Linear Regression - House Price Prediction")
    try:
        file_path = input("Enter CSV file path (House data): ")
        data = pd.read_csv(file_path)

        print("Available columns:", list(data.columns))
        features = input("Enter feature column names (comma-separated): ").split(',')
        target = input("Enter target column (price): ")

        X = data[features]
        y = data[target]

        X = X.fillna(X.mean())
        y = y.fillna(y.mean())

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = LinearRegression()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        print("\n✅ Predictions (first 5):", preds[:5])
        print("✅ Model Score (R²):", model.score(X_test, y_test))

    except Exception as e:
        print("Error:", e)


def matrix_operations():
    print("\n🔢 Matrix Operations Tool")

    def get_matrix(name):
        rows = int(input(f"\nEnter rows for {name}: "))
        cols = int(input(f"Enter columns for {name}: "))
        print(f"Enter values for {name} (row-wise):")
        matrix = [list(map(float, input().split())) for _ in range(rows)]
        return np.array(matrix)

    A = get_matrix("Matrix A")

    print("\nSelect Operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Transpose A\n5. Determinant of A")
    choice = input("Enter choice: ")

    if choice in ['1', '2', '3']:
        B = get_matrix("Matrix B")

    try:
        if choice == '1':
            print("Result:\n", A + B)
        elif choice == '2':
            print("Result:\n", A - B)
        elif choice == '3':
            print("Result:\n", np.dot(A, B))
        elif choice == '4':
            print("Transpose of A:\n", A.T)
        elif choice == '5':
            print("Determinant of A:", np.linalg.det(A))
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)


# 🧭 MAIN MENU
while True:
    print("\n==== PYTHON BEGINNER SLAB ====")
    print("1. CSV Data Analysis & Visualization")
    print("2. Linear Regression (House Price Prediction)")
    print("3. Matrix Operations Tool")
    print("4. Exit")

    opt = input("Select an option (1-4): ")

    if opt == '1':
        data_analysis()
    elif opt == '2':
        linear_regression()
    elif opt == '3':
        matrix_operations()
    elif opt == '4':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("Invalid input. Please choose 1–4.")
