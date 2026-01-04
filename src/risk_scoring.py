def calculate_risk(row):
    """
    Calculates a threat risk score based on behavioral indicators.
    """
    score = 0

    if row["anomaly_flag"] == -1:
        score += 40

    score += row["failed_logins"] * 5
    score += row["login_attempts"] * 2
    score += row["data_accessed_MB"] / 50

    return min(score, 100)

def risk_level(score):
    """
    Classifies threat level based on risk score.
    """
    if score >= 70:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"
