import streamlit as st
import pandas as pd
import numpy as np


# Load student data from CSV file
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Perform basic analysis on grades
def basic_analysis(data):
    st.subheader("Basic Analysis")
    st.write("Average Grades:")
    st.write(data.mean())

    st.write("Highest Grades:")
    st.write(data.max())

    st.write("Lowest Grades:")
    st.write(data.min())


# Main Streamlit app


if __name__ == "__main__":
    main()
