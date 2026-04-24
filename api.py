# FastAPI: The framework we will use to build the web server. 
    # It is currently the industry standard for Python ML APIs because it is blisteringly fast.
# Uvicorn: The actual "server" engine that will run your FastAPI code and listen for internet traffic.
# Pydantic: A data validation tool. If a bank accidentally sends text (like "one thousand") 
    # instead of a number for the transaction amount, Pydantic will catch the error and stop the API from crashing.
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialize the FastAPI app
app = FastAPI(title="Anti-Money Laundering API", description="Real-time fraud detection")

# 2. Load the trained model into memory when the server starts
# (We do this outside the endpoint so it doesn't reload on every single transaction)
print("Loading ML model and test data base...")
model = joblib.load('rf_network_model.joblib')
test_data = pd.read_csv('X_test_network.csv')
test_data.columns = test_data.columns.astype(str)
print("Model and test data loaded successfully!")

# 3. Define the Expected Data Structure using Pydantic
# INITIAL VERSION: This version expects the bank to send all 165 math features + in_degree and out_degree for each transaction.
# This acts as a strict bouncer at the door. It tells the API exactly what features
# it needs to receive from the bank to make a prediction.
# Note: For this example, I'm including just a few features. You would include
# all 165 math features + in_degree and out_degree here!
# class TransactionData(BaseModel):
#     feature_1: float
#     feature_2: float
#     feature_56: float
#     in_degree: float
#     out_degree: float
    # ... (in a real app, you'd list all required features)

# REAL VERSION: our pydantic model to just ask for a transaction ID, since the model will look up the features from the database
class TransactionLookup(BaseModel):
    transaction_id: int

# 4. Create the Prediction Endpoint
# INITIAL VERSION: This version expects the bank to send all 165 math features + in_degree and out_degree for each transaction.
# This is the URL path where the bank will send the data (e.g., website.com/predict)
# @app.post("/predict")
# def predict_fraud(transaction: TransactionData):
#     try:
#         # Convert the incoming JSON data into a dictionary, then a Pandas DataFrame
#         data_dict = transaction.model_dump()
#         df = pd.DataFrame([data_dict])
        
#         # Ask the model for a probability score
#         # [0][1] gets the probability of class 1 (Illicit)
#         fraud_prob = model.predict_proba(df)[0][1] 
        
#         # Create a rule: If probability is > 75%, flag it!
#         is_flagged = bool(fraud_prob > 0.75)
        
#         # Return the final decision back to the bank
#         return {
#             "fraud_probability": round(fraud_prob, 4),
#             "flagged_for_review": is_flagged,
#             "message": "Transaction processed successfully."
#         }
        
#     except Exception as e:
#         # If anything crashes, return a helpful error message
#         raise HTTPException(status_code=400, detail=str(e))

# REAL VERSION: Updated version of the prediction endpoint that looks up features from the database based on transaction ID
@app.post("/predict")
def predict_fraud(lookup: TransactionLookup):
    try:
        # 2. Grab the requested row ID
        row_id = lookup.transaction_id
        # 3. Pull that exact transaction's 167 features from our database
        transaction_features = test_data.iloc[[row_id]]
        # 4. Ask the model for a probability score
        fraud_prob = model.predict_proba(transaction_features)[0][1] 
        is_flagged = bool(fraud_prob > 0.75)
        
        return {
            "transaction_id": row_id,
            "fraud_probability": round(fraud_prob, 4),
            "flagged_for_review": is_flagged,
            "message": "Transaction scored successfully."
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error scoring transaction: {str(e)}")

# to start it run this command in terminal: uvicorn api:app --reload
    # api refers to the name of your file (api.py).
    # app refers to the app = FastAPI(...) variable you created inside the file.
    # --reload tells the server to automatically update if you save changes to your code.

# Open your web browser and go to: http://127.0.0.1:8000/docs