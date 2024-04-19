import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
onlinefood_data= pd.read_csv('C:\\Users\\kavit\\Downloads\\onlinefood.csv')

# Check the first few rows of the dataset
print(onlinefood_data.head())

# Visualize distribution of age
plt.figure(figsize=(10, 6))
sns.histplot(onlinefood_data['Age'], bins=20, kde=False)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Visualize distribution of gender
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=onlinefood_data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Visualize distribution of marital status
plt.figure(figsize=(8, 5))
sns.countplot(x='Marital Status', data=onlinefood_data)
plt.title('Marital Status Distribution')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()

# Visualize distribution of occupation
plt.figure(figsize=(12, 6))
sns.countplot(x='Occupation', data=onlinefood_data)
plt.title('Occupation Distribution')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Visualize monthly income distribution
plt.figure(figsize=(10, 6))
sns.histplot(onlinefood_data['Monthly Income'], bins=20, kde=False)
plt.title('Monthly Income Distribution')
plt.xlabel('Monthly Income')
plt.ylabel('Count')
plt.show()

# Visualize distribution of educational qualifications
plt.figure(figsize=(10, 6))
sns.countplot(x='Educational Qualifications', data=onlinefood_data)
plt.title('Educational Qualifications Distribution')
plt.xlabel('Educational Qualifications')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


