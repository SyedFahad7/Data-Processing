"""
Script: data_processing_script.py

Description:
    This script performs various data processing techniques on a given dataset and generates visualizations using Matplotlib.

Functions:
    1. read_data(file_path)
        - Reads the dataset from the specified file path into a pandas DataFrames.
        - Parameters:
            - file_path (str): The path to the dataset file.
        - Returns:
            - df (DataFrame): The pandas DataFrame containing the dataset.

    2. data_processing(df)
        - Applies several data processing techniques on the input DataFrame.
        - Parameters:
            - df (DataFrame): The input pandas DataFrame.
        - Returns:
            - processed_df (DataFrame): The processed DataFrame after data processing.

    3. generate_visualizations(df)
        - Generates various types of visualizations using Matplotlib based on the input DataFrame.
        - Parameters:
            - df (DataFrame): The pandas DataFrame for visualization.
        - Returns:
            - None

Main Block:
    - The main block of the script reads the dataset using the read_data function.
    - It then performs data processing using the data_processing function to obtain a processed DataFrame.
    - Next, it generates visualizations using the generate_visualizations function to visualize the processed data.

Note:
    - Ensure that the file path to the dataset is correctly specified according to your system configuration.
    - Modify the data processing techniques and visualization types as needed for your specific data analysis requirements.
    - Additional functions or modifications can be made to customize the script further.
"""
#Performing Pandas Techniques 
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('dummy_data.csv')

# Display the first few rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Getting information about the DataFrame
print("\nInformation about the dataset:")
print(df.info())

# Display descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Drop rows with missing values
df.dropna(inplace=True)

# Example: Convert 'time_spent' column to numeric
df['time_spent'] = pd.to_numeric(df['time_spent'], errors='coerce')

#Dropping Ducplicate data 
duplicate_df = df.drop_duplicates()

#removing unnecessary data
df.drop(columns=['indebt','demographics'], inplace=True)

#performing String Operations on String Columns 
df['gender'] = df['gender'].str.upper()

# Save the processed DataFrame to a new CSV file
df.to_csv('processed_data.csv', index=False)

# Performing MATPLOTLIB techniques
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for saving plots without displaying
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('dummy_data.csv')

# Line Plot
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.plot(df['age'], df['time_spent'], marker='o')
plt.xlabel('Age')
plt.ylabel('Time Spent')
plt.title('Time Spent vs. Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('Lineplot.png') 

# Histogram
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.hist(df['age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('histogram.png')  # Save the histogram as a PNG file

# Bar Chart
plt.figure(figsize=(8, 6))  # Adjust figure size
platform_counts = df['platform'].value_counts()
platform_counts.plot(kind='bar')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.title('User Distribution by Platform')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('bar_chart.png')  # Save the bar chart as a PNG file

# Pie Chart
plt.figure(figsize=(8, 8))  # Adjust figure size
gender_counts = df['gender'].value_counts()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('pie_chart.png')  # Save the pie chart as a PNG file

# Box Plot
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.boxplot(df['income'])
plt.ylabel('Income')
plt.title('Income Distribution')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('boxplot.png')  # Save the boxplot as a PNG

# Scatter Plot
plt.figure(figsize=(8, 6))  # Adjust figure size
plt.scatter(df['age'], df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Income vs. Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('scatter_plot.png')  # Save the scatter plot as a PNG file


