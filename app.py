import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Workforce Attrition Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Workforce Attrition Patterns and Risk Hotspot Analysis")
st.markdown("### Palo Alto Networks")

# ----------------------------
# LOAD DATA
# ----------------------------

df = pd.read_csv("cleaned_attrition.csv")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------

st.sidebar.header("Filters")

department = st.sidebar.selectbox(
    "Department",
    ["All"] + list(df["Department"].unique())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + list(df["Gender"].unique())
)

overtime = st.sidebar.selectbox(
    "OverTime",
    ["All"] + list(df["OverTime"].unique())
)

travel = st.sidebar.selectbox(
    "Business Travel",
    ["All"] + list(df["BusinessTravel"].unique())
)

# Apply Filters

filtered_df = df.copy()

if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]

if overtime != "All":
    filtered_df = filtered_df[
        filtered_df["OverTime"] == overtime
    ]

if travel != "All":
    filtered_df = filtered_df[
        filtered_df["BusinessTravel"] == travel
    ]

# ----------------------------
# KPI SECTION
# ----------------------------

total_emp = len(filtered_df)

left_emp = filtered_df["Attrition"].sum()

retained_emp = total_emp - left_emp

attrition_rate = round(
    (left_emp / total_emp) * 100, 2
)

retention_rate = round(
    (retained_emp / total_emp) * 100, 2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", total_emp)
col2.metric("Employees Left", left_emp)
col3.metric("Attrition Rate %", attrition_rate)
col4.metric("Retention Rate %", retention_rate)

st.divider()

# ----------------------------
# ATTRITION DISTRIBUTION
# ----------------------------

st.subheader("Attrition Distribution")

fig, ax = plt.subplots(figsize=(5,4))

sns.countplot(
    x="Attrition",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# ----------------------------
# DEPARTMENT ANALYSIS
# ----------------------------

st.subheader("Department Wise Attrition")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="Department",
    hue="Attrition",
    data=filtered_df,
    ax=ax
)

plt.xticks(rotation=20)

st.pyplot(fig)

# ----------------------------
# JOB ROLE ANALYSIS
# ----------------------------

st.subheader("Job Role Attrition")

fig, ax = plt.subplots(figsize=(10,5))

sns.countplot(
    y="JobRole",
    hue="Attrition",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# ----------------------------
# AGE GROUP ANALYSIS
# ----------------------------

bins = [18,25,35,45,55,65]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "55+"
]

filtered_df["AgeGroup"] = pd.cut(
    filtered_df["Age"],
    bins=bins,
    labels=labels
)

st.subheader("Age Group Attrition")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="AgeGroup",
    hue="Attrition",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# ----------------------------
# OVERTIME ANALYSIS
# ----------------------------

st.subheader("Overtime Impact")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    x="OverTime",
    hue="Attrition",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# ----------------------------
# BUSINESS TRAVEL ANALYSIS
# ----------------------------

st.subheader("Business Travel Impact")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="BusinessTravel",
    hue="Attrition",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# ----------------------------
# DATA PREVIEW
# ----------------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(10))

