import pandas as pd
import numpy as np
import streamlit as st

def analyze_grades(data_file):
    """Analyzes student grades from a CSV file using pandas and NumPy.

    Args:
        data_file (streamlit.uploadedfile.UploadedFile): The uploaded CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing various grade statistics.
    """

    try:
        df = pd.read_csv(data_file)

        # Ensure there's a column containing grades (numerical)
        if not any(pd.api.types.is_numeric_dtype(col) for col in df.columns):
            raise ValueError("No column containing numerical grades found in the CSV file.")

        # Calculate descriptive statistics for each grade column
        grade_stats = df.describe(include='all')  # Include all data types

        # Calculate class average, highest and lowest scores
        class_avg = np.mean(df.filter(like='grade', axis=1))  # Assuming columns with 'grade'
        highest_score = df.filter(like='grade', axis=1).max().max()
        lowest_score = df.filter(like='grade', axis=1).min().min()

        # Create a DataFrame for organized presentation
        stats_df = pd.DataFrame({
            'Metric': ['Class Average', 'Highest Score', 'Lowest Score'],
            'Value': [class_avg, highest_score, lowest_score]
        })

        return pd.concat([grade_stats, stats_df], ignore_index=True)

    except (FileNotFoundError, pd.errors.ParserError, ValueError) as e:
        st.error(f"Error processing CSV file: {e}")
        return pd.DataFrame()

st.title("Student Grade Analyzer")
st.subheader("Upload your CSV file containing student grades")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    results_df = analyze_grades(uploaded_file)

    if not results_df.empty:
        st.success("**File uploaded successfully!**")
        st.write("**Detailed Grade Statistics:**")
        st.dataframe(results_df)
    else:
        st.warning("No data found in the uploaded file.")

st.stop()

