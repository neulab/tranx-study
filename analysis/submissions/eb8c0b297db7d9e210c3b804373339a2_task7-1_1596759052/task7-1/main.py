# Example code, write your program here

# Import pandas library
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt

# Import numpy
import numpy

# Filename definition
fileName = 'shampoo.csv'

# Open CSV using pandas
dataContent = pd.read_csv(fileName)

# Convert date column to datetime
dataContent['Date'] = pd.to_datetime(dataContent.Date)

# Define the plot size
plt.figure(figsize=(10, 6))

# Plot scatter
plt.scatter(dataContent['Date'], dataContent['Sales'], color='purple')

# Plot text
plt.title("Shampoo Sales Trend", fontsize=20)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Sales", fontsize=16)

# Plot parameters
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)

# Save figure
plt.savefig('shampoo.png')