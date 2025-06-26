import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the dataset
df = pd.read_csv("chart.csv")

# Print column names to verify
print("Columns in CSV:", df.columns)

# Ensure correct column names are used
columns_to_use = ['No.', 'Static', 'Dynamic']

# Check if required columns exist
for col in columns_to_use:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in chart.csv")

df = df[columns_to_use]

# Rename 'No.' to a more meaningful name
df.rename(columns={'No.': 'Simulation_Attempt'}, inplace=True)

# Set visualization style
sns.set_style("whitegrid")

# --- 1️⃣ Line Plot ---
plt.figure(figsize=(10, 5))
plt.plot(df['Simulation_Attempt'], df['Static'], marker='o', linestyle='-', label="Static System", color='r')
plt.plot(df['Simulation_Attempt'], df['Dynamic'], marker='s', linestyle='--', label="Dynamic System", color='b')

plt.xlabel('Simulation Attempts')
plt.ylabel('No. of Vehicles Passed')
plt.title('Comparison: Static vs Dynamic Traffic System', fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

# --- 2️⃣ Bar Chart ---
plt.figure(figsize=(10, 5))
width = 0.4
plt.bar(df['Simulation_Attempt'] - width/2, df['Static'], width=width, label='Static', color='r')
plt.bar(df['Simulation_Attempt'] + width/2, df['Dynamic'], width=width, label='Dynamic', color='b')

plt.xlabel('Simulation Attempts')
plt.ylabel('No. of Vehicles Passed')
plt.title('Traffic Flow Comparison - Bar Chart', fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

# --- 3️⃣ Scatter Plot ---
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Simulation_Attempt'], y=df['Static'], label="Static System", color='r', marker='o')
sns.scatterplot(x=df['Simulation_Attempt'], y=df['Dynamic'], label="Dynamic System", color='b', marker='s')

plt.xlabel('Simulation Attempts')
plt.ylabel('No. of Vehicles Passed')
plt.title('Traffic Management Scatter Plot', fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

# --- 4️⃣ 3D Surface Plot ---
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

X = df['Simulation_Attempt']
Y = df['Static']
Z = df['Dynamic']

ax.scatter(X, Y, Z, c=Z, cmap='coolwarm', marker='o')

ax.set_xlabel('Simulation Attempts')
ax.set_ylabel('Static System')
ax.set_zlabel('Dynamic System')
ax.set_title('3D Traffic Flow Visualization')

plt.show()
