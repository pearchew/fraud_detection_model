📂 Project Phases
1. Graph Engineering & Baseline Modeling
Graph Networks: Uses NetworkX to build a directed graph of Bitcoin flows, calculating consolidation and layering metrics for over 200,000 nodes.

Baseline Model: Trains a RandomForestClassifier on the Elliptic dataset, achieving high precision (99%) in flagging illicit activity.

2. Model Auditing & Explainable AI (XAI)
Explainability: Integrates SHAP to provide "evidence bars" for every prediction, showing exactly which features (like a high out-degree) pushed the model toward a "Guilty" verdict.

Fairness Testing: Uses Fairlearn to ensure the model does not unfairly target specific cohorts, such as retail users with lower transaction volumes.

3. Adversarial & Drift Monitoring
Stress Testing: Employs the Adversarial Robustness Toolbox (ART) to simulate "HopSkipJump" evasion attacks, testing if fraudsters can bypass the AI by slightly tweaking their transaction behavior.

Data Drift: Uses Evidently AI to monitor live network data for "Concept Drift," alerting investigators if market shifts (like a "crypto winter") have made the training data obsolete.

4. Deployment
AML API: A production-ready FastAPI server that allows banks or exchanges to look up transaction IDs and receive real-time fraud scores.