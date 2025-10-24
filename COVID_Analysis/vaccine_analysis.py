import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("covid_vaccine_statewise.csv")

# a) Describe the dataset
print("🧾 Dataset Description:\n")
print(df.describe(include='all'))

# Clean data
df = df[df['State'] != 'India']
df.fillna(0, inplace=True)

# b) State-wise First Dose
first_dose = df.groupby("State")["First Dose Administered"].sum().sort_values(ascending=False)
print("\n📊 First Dose:\n", first_dose)
first_dose.plot(kind="barh", figsize=(10, 8), color="skyblue")
plt.title("State-wise First Dose Vaccination")
plt.xlabel("People")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# c) State-wise Second Dose
second_dose = df.groupby("State")["Second Dose Administered"].sum().sort_values(ascending=False)
print("\n📊 Second Dose:\n", second_dose)
second_dose.plot(kind="barh", figsize=(10, 8), color="lightgreen")
plt.title("State-wise Second Dose Vaccination")
plt.xlabel("People")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# d) Male Vaccinations
males = df["Male(Individuals Vaccinated)"].sum()
print(f"\n👨 Males Vaccinated: {int(males):,}")

# e) Female Vaccinations
females = df["Female(Individuals Vaccinated)"].sum()
print(f"👩 Females Vaccinated: {int(females):,}")

# Pie Chart
plt.pie([males, females], labels=["Males", "Females"], colors=["skyblue", "pink"], autopct='%1.1f%%')
plt.title("Gender-wise Vaccination Distribution")
plt.axis('equal')
plt.show()
