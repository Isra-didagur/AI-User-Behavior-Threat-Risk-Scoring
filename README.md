# AI-Powered User Behavior Profiling & Threat Risk Scoring System

## 🔍 Overview
This project implements an **AI-based User Behavior Analytics (UEBA)** system that learns
normal user behavior patterns, detects anomalies, and assigns **dynamic threat risk scores**
for cybersecurity monitoring.

The project demonstrates how **machine learning can be applied to cybersecurity use cases**
such as insider threat detection, compromised account identification, and cloud security
monitoring.

---

## 🧩 Problem Statement
Traditional security systems rely heavily on static rules and known attack signatures.
Such systems struggle to detect **unknown threats, insider attacks, and abnormal user
behavior patterns**.

There is a need for an **AI-driven behavioral analytics system** that can:
- Learn normal behavior automatically
- Detect deviations without labeled attack data
- Prioritize threats using risk scoring

---

## 🎯 Objectives
- Perform user behavior profiling using machine learning
- Detect anomalous behavior patterns using unsupervised AI models
- Generate a dynamic threat risk score for each user
- Map AI outputs to real-world cybersecurity risks

---

## 🧠 Solution Approach
The system follows a modular AI pipeline:

1. **Feature Engineering**
   - Extracts and scales behavioral features such as session duration, login attempts,
     failed logins, and data accessed.

2. **Behavior Profiling**
   - Uses KMeans clustering to group users based on behavioral patterns.

3. **Anomaly Detection**
   - Applies Isolation Forest to identify deviations from normal behavior.

4. **Threat Risk Scoring**
   - Combines anomaly indicators and behavioral signals to generate a risk score.
   - Classifies users into Low, Medium, or High risk categories.

---

## 🏗️ System Architecture
 User Activity Logs
↓
Feature Engineering & Scaling
↓
Behavior Profiling (Clustering)
↓
Anomaly Detection (Isolation Forest)
↓
Threat Risk Scoring
↓
Security Risk Interpretation


---

## 🛠️ Technologies Used
- **Python**
- **Scikit-learn**
- **Pandas & NumPy**
- **Matplotlib**
- **Google Colab / Jupyter Notebook**

---

## 📁 Project Structure
AI-User-Behavior-Threat-Risk-Scoring/
├── notebooks/
│   └── AI_User_Behavior_Threat_Risk_Scoring.ipynb
├── data/
│   └── user_activity_logs.csv
├── src/
│   ├── feature_engineering.py
│   ├── anomaly_detection.py
│   └── risk_scoring.py
├── outputs/
│   └── threat_scores.csv
├── README.md
├── requirements.txt
└── .gitignore




---

## 🔐 Cybersecurity Relevance
This project maps AI outputs to real-world cybersecurity scenarios, including:
- Insider threat detection
- Compromised account identification
- Brute-force login behavior
- Excessive or abnormal data access
- Cloud and SOC security monitoring

The approach aligns with **UEBA (User and Entity Behavior Analytics)** techniques used in
modern SIEM and cloud security platforms.

---

## 📊 Results
- Users with abnormal behavior patterns receive higher threat risk scores
- High-risk users are prioritized for security review
- The system detects suspicious behavior without relying on predefined attack signatures

---

## 🚀 Future Enhancements
- Integration with real cloud logs (AWS CloudTrail / Azure Monitor)
- Real-time threat scoring pipeline
- SIEM integration
- Explainable AI dashboards
- Deep learning–based behavior modeling

---

## 📌 Conclusion
This project demonstrates how **AI-driven behavioral analytics** can enhance cybersecurity
by detecting anomalies and prioritizing risks dynamically. By combining machine learning
with security reasoning, the system highlights the practical value of AI in modern
cloud and enterprise security environments.

---

## 👩‍💻 Author
Developed as part of an **AIML-focused internship project** with a cybersecurity application
to strengthen AI and cloud security skills.
