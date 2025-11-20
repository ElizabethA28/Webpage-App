
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Cardiology Patient Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel file)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file depending on the type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    st.write("### Preview of the Dataset")
    st.subheader("First Few Data Samples")
    st.dataframe(df.head())
    st.subheader("Last Few Data Samples")
    st.dataframe(df.tail())
 

    # Basic Statistics
    st.subheader("Summary of Statistical Data")
    st.write(df.describe())

     # dataset has a date column
    if "date" in df.columns:
        # Convert to datetime
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["month_year"] = df["date"].dt.to_period("M").astype(str)

        monthly = df.groupby("month_year").size().reset_index(name="Admissions")

        # Display table
        st.write("Number of admissions per month:")
        st.dataframe(monthly)

    # Example chart
    st.subheader("Admissions per Month")

    # Create aggregated Count value from dataset
    if "month year" in df.columns:
        monthly = df.groupby("month year").size()

        fig, ax = plt.subplots()
        monthly.plot(ax=ax)
        ax.set_ylabel("Number of Admissions")
        ax.set_xlabel("Month - Year")
        ax.set_title("Admissions Over Time")

        st.pyplot(fig)
    else:
        st.error("Column 'month year' not found in dataset.")
else:
    st.info("Please upload a dataset to begin.")
