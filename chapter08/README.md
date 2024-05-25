# Housing Price Prediction Project 🏡

## Overview 🌟
This project demonstrates the process of building, training, and using a Linear Regression model to predict house prices based on various features. The project is divided into two main scripts: `housing.py` and `load_lr_model.py`.

## Repository Contents 📂

### Scripts Included:
1. **`housing.py`**: This script handles data loading, preprocessing, model training, evaluation, and saving the trained model.
2. **`load_lr_model.py`**: This script loads the saved model and uses it to predict house prices for new data.

### :computer: Script Descriptions

#### `housing.py`
- **Data Loading and Checking**:
  - Loads the housing dataset (`USA_Housing.csv`).
  - Displays dataset information, description, and first few rows.

- **Feature and Target Definition**:
  - Defines features (`X`) and target variable (`y`) for the model.

- **Data Splitting**:
  - Splits data into training and testing sets using `train_test_split`.

- **Model Pipeline**:
  - Creates a pipeline with a `StandardScaler` and `LinearRegression` model.
  - Trains the model using the training data.

- **Model Evaluation**:
  - Prints intercept and coefficients of the trained model.
  - Makes predictions on the test data.
  - Plots and saves the scatter plot of true vs. predicted values.
  - Prints performance metrics: MAE, MSE, R2-score, Explained Variance Score, and Max Error.
  - Performs 10-fold cross-validation and prints the scores.

- **Model Saving and Loading**:
  - Saves the trained model using `joblib`.
  - Demonstrates loading the saved model and making a prediction on new data.

#### `load_lr_model.py`
- **Model Loading and Prediction**:
  - Loads a saved Linear Regression model from a specified path.
  - Validates the new data for prediction.
  - Makes a prediction using the loaded model.
  - Prints the predicted house price.

## Key Features 🌟
- **Data Preprocessing**: Demonstrates loading, checking, and preprocessing of data.
- **Model Training**: Shows how to train a Linear Regression model using a pipeline.
- **Model Evaluation**: Provides comprehensive model evaluation using various metrics and cross-validation.
- **Model Persistence**: Demonstrates saving and loading of trained models.
- **Prediction**: Shows how to make predictions using new data.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: 
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `joblib`

## Usage Example 📋
1. **Running `housing.py`**:
   - Ensure `USA_Housing.csv` is in the same directory as the script.
   - Run the script to train and evaluate the model, and save the trained model.
   ```bash
   python housing.py
   ```
2. ** Running `load_lr_model.py`**:
- Update the `model_path` and `new_data` variables as needed.
- Run the script to load the saved model and make predictions on new data.
   ```bash
   python load_lr_model.py
   ```

## 📸 Ploting the results
![image](https://github.com/pmoschos/python_cf5/assets/133533759/76e38f0b-4fcb-464a-bde3-83c624a06f11)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>