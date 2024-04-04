import pandas as pd
import uuid
import datetime

# Load the dataset
df = pd.read_csv('healthcare_dataset.csv')

# Add a unique ID value to each patient to differentiate patients with the same name
df['PatientID'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Rearrange columns to make the Patient ID come first
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

# Add 'Length of Stay' column to gain inisght on hospital efficiency and patient care

df['Length of Stay'] = [str(datetime.date.fromisoformat(df.iloc[i]["Discharge Date"]) -
                            datetime.date.fromisoformat(df.iloc[i]["Date of Admission"]))[:-9] for i in range(len(df))]

# Add a categorical column that seperates ages by different groups (Adults, Seniors)

df['Age Group'] = ["Adults" if int(
    df.iloc[i]["Age"]) < 65 else "Seniors" for i in range(len(df))]

# Save transformed dataset to a csv in the root directory

df.to_csv("transformed_healthcare_dataset.csv", index=False)
