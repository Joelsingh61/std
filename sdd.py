import streamlit as st
import pandas as pd
import numpy as np  # Added for standard deviation

def analyze_student_grades(df):
    """Analyzes student grades from a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing student data.

    Returns:
        None: Prints the analysis results to the Streamlit app.
    """

    # Descriptive statistics
    st.header("Descriptive Statistics")
    st.write(df.describe(include='all'))  # Include all data types

    # Number of students
    num_students = df.shape[0]
    st.write(f"Number of Students: {num_students}")

    # Average grade
    avg_grade = df['Grade'].mean()
    st.write(f"Average Grade: {avg_grade:.2f}")

    # Standard deviation of grades (using numpy)
    std_dev = np.std(df['Grade'])
    st.write(f"Standard Deviation: {std_dev:.2f}")

    # Highest and lowest grades
    highest_grade = df['Grade'].max()
    lowest_grade = df['Grade'].min()
    st.write(f"Highest Grade: {highest_grade:.2f}")
    st.write(f"Lowest Grade: {lowest_grade:.2f}")

    # Distribution of grades (histogram)
    st.header("Distribution of Grades")
    fig, ax = plt.subplots()
    ax.hist(df['Grade'], bins=10, edgecolor='black')  # Adjust bins as needed
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Student Grades')
    st.pyplot(fig)

def main():
    """The main function that runs the Streamlit app."""

    st.title("Student Grade Analyzer")
    uploaded_file = st.file_uploader("Upload CSV File", type='csv')

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Basic validation (assuming 'Grade' is the column name)
            if 'Grade' not in df.columns:
                st.error("Error: The uploaded CSV file must contain a column named 'Grade'.")
            else:
                # Ensure 'Grade' column has numeric values (using try-except)
                try:
                    df['Grade'] = pd.to_numeric(df['Grade'])
                    analyze_student_grades(df.copy())  # Avoid modifying original DataFrame
                except ValueError:
                    st.error("Error: The 'Grade' column must contain valid numeric values.")

        except pd.errors.ParserError:
            st.error("Error: Invalid CSV file format. Please ensure it's a valid CSV file.")

if __name__ == "__main__":
    main()
