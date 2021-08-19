"""
CP1404/CP5632 - Practical
Electricity bill calculator with tariff adjustment
"""

est_bill = 0
print("Electricity bill estimator 2.0")
tariff = input("Which tariff 11 or 31:")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
if tariff == "11":
    daily_use = float(input("Enter daily use in kwh: "))
    billing_days = float(input("Enter number of billing days: "))
    est_bill = daily_use * billing_days * TARIFF_11
elif tariff == "31":
    daily_use = float(input("Enter daily use in kwh: "))
    billing_days = float(input("Enter number of billing days: "))
    est_bill = daily_use * billing_days * TARIFF_31
else:
    print("Invalid Tariff")
print("Estimated bill: ${:.2f}".format(est_bill))
