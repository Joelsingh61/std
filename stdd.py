import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualize grade distribution
def visualize_grade_distribution(data):
    st.subheader("Grade Distribution")

    # Count grade occurrences
    grade_counts = data['Grade'].value_counts()

    # Plot grade distribution
    fig, ax = plt.subplots()
    ax.bar(grade_counts.index, grade_counts.values)
    ax.set_xlabel('Grades')
    ax.set_ylabel('Number of Students')
    ax.set_title('Grade Distribution')
    st.pyplot(fig)

# Calculate and visualize grade correlation
def grade_correlation(data):
    st.subheader("Grade Correlation")

    # Calculate correlation matrix
    corr_matrix = data.corr()

    # Plot correlation heatmap
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Grade Correlation Heatmap')
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Student Grade Analyzer")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        data = load_data(uploaded_file)

        # Show basic information about the data
        st.subheader("Student Data")
        st.write(data.head())
        st.write(f"Number of Students: {len(data)}")

        # Perform analysis functions
        basic_analysis(data)
        visualize_grade_distribution(data)
        grade_correlation(data)

if __name__ == "__main__":
    main()
