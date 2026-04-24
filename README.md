# Goal 

## Phase 1: Algorithmic Advancements (The "Brain")
- Transition to Graph Networks for AML: Fraudsters often move money through complex networks to obscure its origin. You should explore datasets like the Elliptic Data Set (Bitcoin transactions) or PaySim (mobile money). Apply Graph Neural Networks (GNNs) or extract network-based features (e.g., PageRank, in-degree/out-degree velocity) to feed into your XGBoost/LightGBM models.
- Explainable AI (XAI): Financial regulators (like the FCA in the UK) require that automated decisions be explainable. You cannot just block a transaction without a reason. Integrate SHAP (SHapley Additive exPlanations) or LIME into your pipeline. This will break down exactly which features (e.g., Time, Amount, or a specific PCA feature) pushed the model's probability score over your 0.50 threshold.
**WIP: Sequential/Time-Series Analysis: A user swiping their card in London and then in Tokyo 10 minutes later is a massive red flag. Implement features that capture the velocity of transactions (e.g., "amount spent in the last 1 hour").**

Phase 2: MLOps and Engineering (The "Muscles")
- API Deployment: Wrap your serialized best_fraud_model.joblib and robust_scaler.joblib in a FastAPI or Flask application. The API should receive a transaction payload, transform the Amount and Time using the loaded scaler, pass it to the model, and return a JSON response with the fraud probability.
- Concept Drift Monitoring: Fraudsters change their tactics. Use tools like Evidently AI or Prometheus/Grafana to monitor the incoming data distribution and model performance over time to detect when the model needs retraining.

Phase 3: The Proposed Product Vision (The "Face")
What the product looks like:
- The User: A human Fraud Analyst or AML Investigator at a bank (e.g., Monzo, Revolut).
- The Interface: A web dashboard built using Streamlit, Dash, or React.

The Workflow: 
1.  Live Feed: The dashboard shows a live feed of transactions coming in via your Kafka stream.
2.  Alert Queue: Transactions that score above a specific probability threshold (e.g., >85%) are automatically blocked, while borderline transactions (e.g., 50%-85%) are flagged and sent to a manual "Investigator Queue."
3.  Deep Dive & XAI: When the investigator clicks on a flagged transaction, they see a "Trust Score." More importantly, they see a SHAP waterfall plot that translates the model's math into plain English (e.g., "This transaction is highly risky because the amount ($4,500) deviates significantly from the user's usual spending behavior, and it is part of a 3-node money transfer loop").
4.  Graph Visualization: The dashboard displays a localized visual graph showing the flagged account's connections to other suspicious accounts, aiding the AML investigation.