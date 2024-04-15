
import matplotlib.pyplot as plt
import pandas as pd
#
# import numpy as np

#
# Read the data from the file
#
# df = pd.read_csv('DATA_TXT_CLEAN/RUN010_dE2E5c.txt', sep=r'\s+', header=None, names=['x', 'y', 'z'])

# Read the original file
df_original = pd.read_csv('DATA_TXT_CLEAN/RUN010_dE2E5c.txt', sep=r'\s+', header=None, names=['x', 'y', 'z'])

# Create the original histogram
plt.figure(figsize=(10, 10))
plt.hist2d(df_original['x'], df_original['y'], bins=8000, cmap='Blues', alpha=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Original Histogram')
plt.colorbar()
plt.tight_layout()

# Define the bin of interest
bin_of_interest = 300

# Filter the data to get the events in the bin of interest
df_filtered = df_original[(df_original['x'] >= bin_of_interest) & (df_original['x'] < bin_of_interest + 10)]

# Plot the histogram of y values for the events in the bin of interest
plt.figure(figsize=(10, 5))
plt.hist(df_filtered['y'], bins=8000, alpha=0.5, color='r')
plt.xlabel('Y')
plt.ylabel('Number of events')
plt.title('Histogram of Y values in bin {}'.format(bin_of_interest))
plt.tight_layout()

# Show the plots
plt.show()

#
# plt.savefig('histogram_no_axes.png', bbox_inches='tight', dpi=600)
