#Synthetic Data Generation
#Egyptian healthcare data is synthetically generated with realistic regional, facility, and epidemiological distributions.
#Key conditions weighted by Egypt-specific prevalence: Diabetes (~15-32%), Hypertension (~25-45%), Obesity (~34%).

import numpy as np
import pandas as pd

np.random.seed(42)
N = 5000

regions = ['Cairo/Giza', 'Alexandria', 'Upper Egypt', 'Delta']
region_weights = [0.40, 0.25, 0.20, 0.15]
facility_types = ['Government Hospital', 'Private Clinic', 'University Hospital', 'Health Insurance Entity']
facility_weights = [0.45, 0.30, 0.15, 0.10]

region = np.random.choice(regions, N, p=region_weights)
facility = np.random.choice(facility_types, N, p=facility_weights)
age = np.random.randint(18, 80, N)
sex = np.random.choice(['Male', 'Female'], N, p=[0.51, 0.49])
num_dependents = np.random.choice([0,1,2,3,4,5], N, p=[0.25,0.25,0.25,0.15,0.07,0.03])
bmi = np.clip(np.random.normal(27.5, 6.0, N), 15, 50)
obese = (bmi >= 30).astype(int)
diabetes = (np.random.rand(N) < (0.15 + 0.05*obese + 0.003*age)).astype(int)
hypertension = (np.random.rand(N) < (0.25 + 0.04*obese + 0.004*age)).astype(int)
smoker = np.random.choice([0,1], N, p=[0.75, 0.25])
insured = np.where(facility == 'Health Insurance Entity', 1,
          np.where(facility == 'Government Hospital', np.random.choice([0,1], N, p=[0.6,0.4]),
          np.where(facility == 'University Hospital', np.random.choice([0,1], N, p=[0.5,0.5]),
          np.random.choice([0,1], N, p=[0.85,0.15]))))

base_cost = np.where(facility == 'Private Clinic', np.random.normal(8000, 2000, N),
            np.where(facility == 'University Hospital', np.random.normal(5000, 1500, N),
            np.where(facility == 'Government Hospital', np.random.normal(2500, 800, N),
            np.random.normal(3500, 1000, N))))

charges = (base_cost + age*120 + bmi*200
           + diabetes*np.random.normal(6000,1000,N)
           + hypertension*np.random.normal(4000,800,N)
           + smoker*np.random.normal(5000,1200,N)
           + num_dependents*500
           + obese*np.random.normal(3000,700,N)
           - insured*np.random.normal(2000,500,N)
           + np.random.normal(0, 1500, N))

region_multiplier = {'Cairo/Giza':1.15,'Alexandria':1.05,'Upper Egypt':0.80,'Delta':0.90}
charges = charges * np.array([region_multiplier[r] for r in region])
charges = np.clip(charges, 500, 120000).round(2)

df = pd.DataFrame({
    'patient_id': [f'EGY-{str(i+1).zfill(5)}' for i in range(N)],
    'age': age, 'sex': sex, 'bmi': bmi.round(1), 'num_dependents': num_dependents,
    'smoker': smoker, 'diabetes': diabetes, 'hypertension': hypertension,
    'obese': obese, 'region': region, 'facility_type': facility,
    'insured': insured, 'annual_charges_egp': charges
})

df.to_csv("egypt_healthcare_synthetic_data.csv", index=False)
