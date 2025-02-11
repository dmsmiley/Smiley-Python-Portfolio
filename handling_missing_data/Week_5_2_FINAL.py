import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import streamlit as st  # For creating the interactive app
import seaborn as sns  # For easy dataset loading and visualizations
import matplotlib.pyplot as plt  # For plotting

# ------------------------------------------------------------------------------
# Lecture: Data Validation, Outliers, Inconsistencies & Errors in Data
# ------------------------------------------------------------------------------
st.title("Data Validation & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Outlier Detection:** Using boxplots and the IQR method.
- **Identifying Inconsistencies & Errors:** Spotting duplicates and unexpected values.
""")

# ------------------------------------------------------------------------------
# Load a different dataset: the 'tips' dataset from seaborn
# ------------------------------------------------------------------------------
df = sns.load_dataset("tips")

st.header("1. Data Validation")
st.subheader("Data Overview")
st.write("First few rows of the dataset:")
st.dataframe(df.head())

st.subheader("Data Types & Missing Values")
st.write("Data Types:")
st.write(df.dtypes)
st.write("Missing Values per Column:")
st.write(df.isnull().sum())

# ------------------------------------------------------------------------------
# Detecting Outliers in a Numerical Column ('total_bill')
# ------------------------------------------------------------------------------
st.header("2. Detecting Outliers")
st.subheader("Boxplot for 'total_bill'")

# Create a boxplot for 'total_bill'
fig1, ax1 = plt.subplots()
sns.boxplot(x=df["total_bill"], ax=ax1)
ax1.set_title("Boxplot of Total Bill")
st.pyplot(fig1)

# Calculate IQR for 'total_bill' to identify outliers
Q1 = df["total_bill"].quantile(0.25)
Q3 = df["total_bill"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

st.write(f"Lower Bound: {lower_bound:.2f}")
st.write(f"Upper Bound: {upper_bound:.2f}")

# Identify outliers in 'total_bill'
outliers = df[(df["total_bill"] < lower_bound) | (df["total_bill"] > upper_bound)]
st.write("Rows with outliers in 'total_bill':")
st.dataframe(outliers)

# ------------------------------------------------------------------------------
# Identifying Inconsistencies and Errors
# ------------------------------------------------------------------------------
st.header("3. Identifying Inconsistencies and Errors")
st.subheader("Duplicate Records")

# Check for duplicate rows in the dataset
duplicate_count = df.duplicated().sum()
st.write(f"Number of duplicate rows: {duplicate_count}")

# For demonstration, let's simulate an inconsistency:
# Assume that a negative tip value is an error.
st.subheader("Checking for Unexpected Values in 'tip'")
# Simulate an error by injecting a negative tip value into a copy of the dataset
df_error = df.copy()
if not df_error.empty:
    df_error.loc[df_error.index[0], "tip"] = -5  # Introduce a negative tip value

# Check for negative tip values
negative_tips = df_error[df_error["tip"] < 0]
if negative_tips.empty:
    st.write("No negative tip values found.")
else:
    st.write("Negative tip values detected:")
    st.dataframe(negative_tips)

# ------------------------------------------------------------------------------
# Final Notes
# ------------------------------------------------------------------------------
st.header("Conclusion")
st.markdown("""
Validating your data is a crucial first step in any analysis.  
By checking for data type mismatches, missing values, outliers, duplicates,  
and other inconsistencies, you can ensure that your insights are based on reliable data.
""")
