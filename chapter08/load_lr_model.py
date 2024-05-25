from joblib import load
import numpy as np

def predict_house_price(model_path, new_data):
    """
    Predicts the house price using a pre-trained linear regression model.

    Parameters:
    model_path (str): The path to the saved model.
    new_data (list): A list of feature values in the following order:
        'Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population'

    Returns:
    float: The predicted house price.
    """
    try:
        # Load the saved linear model
        loaded_linear_model = load(model_path)
        print("Model loaded successfully.")

        # Validate new_data
        if len(new_data) != 5:
            raise ValueError("New data must contain exactly 5 feature values.")

        # Ensure the new data is in the correct shape (2-dimensional array)
        reshape_data = np.array(new_data).reshape(1, -1)

        # Make the prediction
        price_predicted = loaded_linear_model.predict(reshape_data)

        # Display the predicted price
        print(f"Predicted house price: ${price_predicted[0]:,.2f}")
        return price_predicted[0]
    
    except FileNotFoundError:
        print("The model file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
model_path = 'linear_model.joblib'
new_data = [80000, 5, 7, 4, 25000]  # Example new data

# Predict and display the house price
predicted_price = predict_house_price(model_path, new_data)

