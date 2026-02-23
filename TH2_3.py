import pandas as pd
import numpy as np

# =========================
# Sample historical profile
# =========================

historical_profile = {
    "avg_amount": 5000000,        # avg transaction amount
    "std_amount": 2000000,
    "avg_daily_tx": 3,
    "known_ips": ["192.168.1.10"],
    "known_devices": ["iPhone15"],
    "home_lat": 10.762622,
    "home_lon": 106.660172,
    "monthly_income": 15000000
}

# =========================
# Utility: distance check
# =========================

def geo_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# =========================
# TH2: Point Anomaly Detection
# =========================

def detect_point_anomaly(tx, profile):
    risk_score = 0
    reasons = []

    # Amount anomaly (Z-score)
    z = abs(tx["amount"] - profile["avg_amount"]) / profile["std_amount"]
    if z > 3:
        risk_score += 0.3
        reasons.append("Amount anomaly (Z-score > 3)")

    # Income mismatch
    if tx["amount"] > profile["monthly_income"]:
        risk_score += 0.2
        reasons.append("Transaction exceeds monthly income")

    # IP anomaly
    if tx["ip"] not in profile["known_ips"]:
        risk_score += 0.15
        reasons.append("Unknown IP")

    # Device anomaly
    if tx["device"] not in profile["known_devices"]:
        risk_score += 0.15
        reasons.append("Unknown device")

    # Geo anomaly
    dist = geo_distance(
        tx["lat"], tx["lon"],
        profile["home_lat"], profile["home_lon"]
    )
    if dist > 0.5:
        risk_score += 0.2
        reasons.append("Geolocation deviation")

    return min(risk_score, 1.0), reasons


# =========================
# TH3: Exoneration Layer
# =========================

def exoneration_layer(tx, risk_score, reasons):
    """
    Reduce false positives if legitimate context exists
    """

    # Example legitimate context flags
    if tx.get("travel_flag"):
        risk_score -= 0.2
        reasons.append("Travel context verified")

    if tx.get("salary_bonus"):
        risk_score -= 0.15
        reasons.append("Income spike justified")

    if tx.get("verified_asset_purchase"):
        risk_score -= 0.2
        reasons.append("Asset purchase documented")

    return max(risk_score, 0), reasons


# =========================
# Example Transaction
# =========================

transaction = {
    "amount": 25000000,
    "ip": "8.8.8.8",
    "device": "AndroidX",
    "lat": 21.0278,
    "lon": 105.8342,
    "travel_flag": True,
    "salary_bonus": False,
    "verified_asset_purchase": False
}

# Run TH2
risk, reasons = detect_point_anomaly(transaction, historical_profile)

# Run TH3
final_risk, final_reasons = exoneration_layer(transaction, risk, reasons)

print("Initial Risk Score:", risk)
print("Final Risk Score after Exoneration:", final_risk)
print("Reasons:")
for r in final_reasons:
    print("-", r)