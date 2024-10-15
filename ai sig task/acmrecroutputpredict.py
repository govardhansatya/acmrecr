import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dataset
data = [
    [0.0, 0.0, 0.0], [0.5, 1.5, 23.4], [1.2, 2.3, 45.6],
    [1.8, 3.7, 12.1], [2.4, 4.2, 78.9], [2.9, 5.1, 34.5],
    [3.5, 6.4, 56.7], [4.1, 7.8, 67.8], [4.7, 8.5, 89.0],
    [5.2, 9.1, 12.3], [5.8, 1.0, 45.6], [6.3, 2.4, 78.9],
    [6.9, 3.1, 34.5], [7.4, 4.6, 56.7], [8.0, 5.2, 67.8],
    [8.6, 6.8, 89.0], [9.1, 7.3, 12.3], [9.7, 8.9, 45.6],
    [10.0, 9.0, 78.9], [10.5, 0.5, 34.5]
]

data = np.array(data)
X = data[:, :2]
y = data[:, 2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#mse = mean_squared_error(y_test, y_pred)
#print(f"Mean Squared Error: {mse}")

def predict_new_data():
    try:
        n = int(input("Enter the number of new data points: "))
        new_data = []
        for i in range(n):
            x1 = float(input(f"Enter the first input for data point {i+1}: "))
            x2 = float(input(f"Enter the second input for data point {i+1}: "))
            new_data.append([x1, x2])
        new_data = np.array(new_data)
        predictions = model.predict(new_data)
        for i, prediction in enumerate(predictions):
            print(f"Prediction for data point {i+1}: {prediction}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

predict_new_data()