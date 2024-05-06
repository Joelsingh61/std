import streamlit as st
import pandas as pd

# Load student data from CSV file
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Main function to perform analysis
def perform_analysis(data):
    st.subheader("Student Data")
    st.write(data.head())

    st.subheader("Basic Analysis")
    st.write("Average Grades:")
    st.write(data.mean())

    st.write("Highest Grades:")
    st.write(data.max())

    st.write("Lowest Grades:")
    st.write(data.min())

    st.subheader("Grade Distribution")
    grade_distribution = data['Grade'].value_counts()
    st.write(grade_distribution)

# Streamlit app
def main():
    st.title("Student Grade Analyzer")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        perform_analysis(data)

if __name__ == "__main__":
    main()
