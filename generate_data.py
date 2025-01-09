import pandas as pd
import numpy as np
import random

def generate_patient_usage_data(n_patient=200):
    # Define age groups
    age_groups = {
        "0-19": (0, 19),
        "20-39": (20, 39),
        "40-59": (40, 59),
        "60-79": (60, 79),
        "80+": (80, 120)
    }

    # Generate patient demographic data
    patients = {
        "PatientID": [f"P{str(i).zfill(4)}" for i in range(1, n_patient + 1)],
        "Age": np.random.randint(15, 85, n_patient),
        "Gender": np.random.choice(["Male", "Female"], n_patient, p=[0.4, 0.6]),
        "Province": np.random.choice(
            ["Bangkok", "Chiang Mai", "Khon Kaen", "Phuket", "Songkhla", "Nakhon Ratchasima", "Nonthaburi"],
            n_patient
        ),
        "HealthCondition": np.random.choice(
            ["Diabetes", "Hypertension", "Healthy", "Asthma", "Heart Disease", "Obesity"],
            n_patient
        )
    }

    # Assign age groups
    patients["AgeGroup"] = [
        next(group for group, (low, high) in age_groups.items() if low <= age <= high)
        for age in patients["Age"]
    ]

    # Generate monthly usage data over 5 years (60 months)
    years = 5
    months_per_year = 12
    total_months = years * months_per_year

    usage_data = []
    for patient_id in patients["PatientID"]:
        for month in range(total_months):
            year = 2025 - (month // 12)
            month_num = (month % 12) + 1
            usage = random.randint(0, 10)  # Random usage frequency (times per month)
            usage_data.append({"PatientID": patient_id, "Year": year, "Month": month_num, "UsageFrequency": usage})

    # Create DataFrames
    patients_df = pd.DataFrame(patients)
    usage_df = pd.DataFrame(usage_data)

    # Merge data for analysis
    merged_df = usage_df.merge(patients_df, on="PatientID")

    # Save the data to CSV files
    file_path_patients = "data/Patient_Demographics_Thailand.csv"
    file_path_usage = "data/Monthly_Usage_5Years.csv"
    file_path_merged = "data/Merged_Usage_Patient_Data.csv"

    patients_df.to_csv(file_path_patients, index=False)
    usage_df.to_csv(file_path_usage, index=False)
    merged_df.to_csv(file_path_merged, index=False)

    return file_path_patients, file_path_usage, file_path_merged

# Example usage
file_path_patients, file_path_usage, file_path_merged = generate_patient_usage_data(n_patient=300)
file_path_patients, file_path_usage, file_path_merged
