import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot(df['age'], df['time_spent'], marker='o')
plt.xlabel('Age')
plt.ylabel('Time Spent')
plt.title('Time Spent vs. Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('Lineplot.png') 

# Histogram
plt.hist(df['age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('histogram.png')  # Save the histogram as a PNG file

# Bar Chart
platform_counts = df['platform'].value_counts()
platform_counts.plot(kind='bar')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.title('User Distribution by Platform')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('bar_chart.png')  # Save the bar chart as a PNG file

# Pie Chart
gender_counts = df['gender'].value_counts()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('pie_chart.png')  # Save the pie chart as a PNG file

# Box Plot
plt.boxplot(df['income'])
plt.ylabel('Income')
plt.title('Income Distribution')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('boxplot.png')  # Save the boxplot as a PNG

# Scatter Plot
plt.scatter(df['age'], df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Income vs. Age')
plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('scatter_plot.png')  # Save the scatter plot as a PNG file

