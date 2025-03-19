import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df=pd.read_csv("Icecream Sales wr Rain and Temperature.csv")
# Selecting features and target variable
X = df[['Temperature (F)']]  # Independent variable
y = df['Ice Cream Sales ($,thousands)']  # Dependent variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting values
y_pred = model.predict(X_test)

# Visualizing the regression line
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_test.values.flatten(), y=y_test, label="Actual Data", color="blue")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("Temperature (F)")
plt.ylabel("Ice Cream Sales ($,thousands)")
plt.title("Linear Regression: Ice Cream Sales vs Temperature")
plt.legend()
plt.show()

# Printing model coefficients
model.coef_, model.intercept_
