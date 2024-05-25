import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.metrics import r2_score
from joblib import dump, load
import seaborn as sns

# Loading and checking our data
USAHousing = pd.read_csv('USA_Housing.csv')

# Print dataset info
print("Dataset Information:")
print(USAHousing.info())
print("\nDataset Description:")
print(USAHousing.describe())
print("\nFirst few rows of the dataset:")
print(USAHousing.head())

# Optional: Uncomment to see initial data plots
# sns.pairplot(USAHousing)
# plt.savefig('pairplot.png')  # Saving the pairplot
# plt.show()

# Defining features and target variable
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 
                'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 
                'Area Population']]
y = USAHousing['Price']

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Creating a pipeline with a scaler and a linear regression model
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Feature scaling
    ('linear_model', LinearRegression())
])

# Training the model
pipeline.fit(X_train, y_train)

# Model evaluation

# Print intercept and coefficients
print(f"\nIntercept: {pipeline.named_steps['linear_model'].intercept_}")

coeff_df = pd.DataFrame(pipeline.named_steps['linear_model'].coef_, X.columns, columns=['Coefficient'])
print("\nCoefficients:")
print(coeff_df)

# Making predictions
predictions = pipeline.predict(X_test)

# Plotting and saving the scatter plot for predictions
plt.scatter(y_test, predictions, color='red', label="Predictions")
plt.plot(y_test, y_test, color='blue', label='Actual Values')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.savefig('predictions_vs_actuals.png')  # Saving the plot
plt.show()

# Performance metrics
print("\nPerformance Metrics:")
print("MAE:", metrics.mean_absolute_error(y_test, predictions))
print("MSE:", metrics.mean_squared_error(y_test, predictions))
print("R2-score:", r2_score(y_test, predictions))
print("Explained Variance Score:", metrics.explained_variance_score(y_test, predictions))
print("Max Error:", metrics.max_error(y_test, predictions))

# Cross-validation score
cv_scores = cross_val_score(pipeline, X, y, cv=10)
print(f"\nCross-validation scores (10-fold): {cv_scores}")
print(f"Mean cross-validation score: {cv_scores.mean()}")

# Save the model for future use
dump(pipeline, 'linear_model_pipeline.joblib')

# Loading the 'saved' linear model
try:
    loaded_pipeline = load('linear_model_pipeline.joblib')
    # Predicting on new data
    new_data = [80000, 7, 7, 4, 25000]
    reshape_data = np.array(new_data).reshape(1, -1)
    price_predicted = loaded_pipeline.predict(reshape_data)

    # Display the predicted price
    print(f"\nPredicted house price: ${price_predicted[0]:,.2f}")
except Exception as e:
    print(f"An error occurred: {e}")
