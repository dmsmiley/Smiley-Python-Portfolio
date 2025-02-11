import pandas as pd  # Data handling
import seaborn as sns  # Plotting library
import matplotlib.pyplot as plt  # Plotting library
import streamlit as st  # Web app framework

# Load the dataset
df = pd.read_csv("titanic.csv")

# Show summary statistics
st.write("Summary Statistics")
st.dataframe(df.describe())

# Show count of missing values per column
st.write("Number of Missing Values by Column")


# Display a heatmap of missing values
st.write("Heatmap of Missing Values")


# Section for handling missing data
st.subheader("Handle Missing Data")

# Let the user choose a numeric column and a method for filling missing data

# Work on a copy to keep the original data intact

# Create two side-by-side columns for displaying results

# Apply the selected method to handle missing data


# Original data distribution and stats

# Cleaned data distribution and stats

