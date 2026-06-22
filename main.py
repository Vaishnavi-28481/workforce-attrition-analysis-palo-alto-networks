import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("Palo Alto Networks.csv")

print(df.shape)

print(df.info())

print(df.isnull().sum())

print(df.duplicated().sum())

total_emp = len(df)

left_emp = df["Attrition"].sum()

retained_emp = total_emp - left_emp

attrition_rate = (left_emp / total_emp) * 100

print("Total Employees :", total_emp)
print("Employees Left :", left_emp)
print("Retained Employees :", retained_emp)
print("Attrition Rate :", round(attrition_rate,2), "%")

plt.figure(figsize=(6,4))

sns.countplot(x="Attrition", data=df)

plt.title("Attrition Distribution")
plt.savefig(
    "images/01_attrition_distribution.png",
    bbox_inches="tight"
)
plt.show()


dept_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

dept_attrition.plot(
    kind="bar",
    figsize=(7,4)
)

plt.title("Department Wise Attrition")
plt.savefig(
    "images/02_department_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(9,5))

sns.countplot(
    y="JobRole",
    hue="Attrition",
    data=df
)

plt.title("Job Role Attrition")
plt.savefig(
    "images/03_job_role_attrition.png",
    bbox_inches="tight"
)
plt.show()

bins = [18,25,35,45,55,65]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "55+"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

plt.figure(figsize=(8,5))

sns.countplot(
    x="AgeGroup",
    hue="Attrition",
    data=df
)

plt.title("Age Group Attrition")
plt.savefig(
    "images/04_age_group_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(6,4))

sns.countplot(
    x="Gender",
    hue="Attrition",
    data=df
)

plt.title("Gender Attrition")
plt.savefig(
    "images/05_gender_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(7,5))

sns.countplot(
    x="MaritalStatus",
    hue="Attrition",
    data=df
)

plt.title("Marital Status Attrition")
plt.savefig(
    "images/06_marital_status_attrition.png",
    bbox_inches="tight"
)
plt.show()

plt.figure(figsize=(6,4))

sns.countplot(
    x="OverTime",
    hue="Attrition",
    data=df
)

plt.title("Overtime Impact")
plt.savefig(
    "images/07_overtime_impact.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(8,5))

sns.countplot(
    x="BusinessTravel",
    hue="Attrition",
    data=df
)

plt.title("Business Travel vs Attrition")
plt.savefig(
    "images/08_business_travel_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(8,5))

sns.boxplot(
    x="Attrition",
    y="YearsAtCompany",
    data=df
)

plt.title("Years At Company vs Attrition")
plt.savefig(
    "images/09_years_at_company_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(8,5))

sns.boxplot(
    x="Attrition",
    y="YearsSinceLastPromotion",
    data=df
)

plt.title("Promotion Delay vs Attrition")
plt.savefig(
    "images/10_promotion_delay_attrition.png",
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(12,8))

corr = df.select_dtypes(include=np.number).corr()

sns.heatmap(
    corr,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig(
    "images/11_correlation_heatmap.png",
    bbox_inches="tight"
)
plt.show()



df.to_csv("cleaned_attrition.csv", index=False)