import csv
import random
from faker import Faker

fake = Faker()

path = r"C:\Users\ASUS\OneDrive - National Center for Educational Technologies\Desktop\DSA files\patient_visits.csv"

department_diagnoses = {
    "Cardiology": ["Hypertension", "Heart Failure", "Arrhythmia", "Myocardial Infarction"],
    "Neurology": ["Migraine", "Stroke", "Epilepsy", "Parkinson's Disease"],
    "Pediatrics": ["Asthma", "Bronchitis", "Chickenpox", "Allergies"],
    "Oncology": ["Breast Cancer", "Lung Cancer", "Leukemia", "Lymphoma"],
    "Orthopedics": ["Fracture", "Arthritis", "Back Pain", "Osteoporosis"]
}


num_records = 1000000
num_patients = 500
num_doctors = 100

with open(path, "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "visit_id", "patient_id", "doctor_id", "department", "diagnosis",
        "treatment_cost", "number_of_visits", "risk_score", "referral_doctor", "outcome_score"
    ])
    
    for i in range(1, num_records + 1):
        visit_id = i
        patient_id = random.randint(1, num_patients)
        doctor_id = random.randint(1, num_doctors)
        department = random.choice(list(department_diagnoses.keys()))
        diagnosis = random.choice(department_diagnoses[department])
        treatment_cost = round(random.uniform(100, 20000), 2)
        number_of_visits = random.randint(1, 20)
        risk_score = round(random.uniform(0, 1), 2)
        referral_doctor = random.randint(1, num_doctors)
        outcome_score = round(random.uniform(0, 100), 2)
        
        writer.writerow([
            visit_id, patient_id, doctor_id, department, diagnosis,
            treatment_cost, number_of_visits, risk_score, referral_doctor, outcome_score
        ])
