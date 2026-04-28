import streamlit as st
import requests

# 1. Set up the page
st.set_page_config(page_title="AML Investigator Copilot", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ AML Investigator Copilot")
st.write("Enter a Bitcoin Transaction ID to scan the network for money laundering.")

# 2. Create an input box for the user
transaction_id = st.number_input("Transaction ID (Row Number)", min_value=0, value=4, step=1)

# 3. Create an "Investigate" button
if st.button("Scan Transaction"):
    
    # 4. When clicked, send the data to your FastAPI server!
    api_url = "http://127.0.0.1:8000/predict"
    payload = {"transaction_id": transaction_id}
    
    with st.spinner("Analyzing network features..."):
        try:
            # Send the request and get the JSON response
            response = requests.post(api_url, json=payload)
            result = response.json()
            
            # 5. Display the results beautifully
            st.divider()
            
            # Convert probability to a percentage
            prob_percent = result['fraud_probability'] * 100
            
            # Display metrics
            col1, col2 = st.columns(2)
            col1.metric("Fraud Probability", f"{prob_percent:.2f}%")
            
            if result['flagged_for_review']:
                col2.error("🚨 HIGH RISK: FLAGGED FOR REVIEW")
                st.warning("This transaction exceeds the 75% risk threshold. Recommend freezing assets and generating SHAP report.")
            else:
                col2.success("✅ LOW RISK: CLEARED")
                st.info("Transaction appears normal based on network topology.")
                
        except Exception as e:
            st.error(f"Failed to connect to the API. Is your FastAPI server running? Error: {e}")