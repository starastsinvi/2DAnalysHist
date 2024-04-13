import matplotlib.pyplot as plt
import numpy as np

data1_x = [1, 2, 3]
data1_y = [3, 4, 3]
data2_x = [1, 2, 3]
data2_y = [4, 5, 6]

# filepath1 = './DATA_TXT/RUN010_dE2.txt'
# filepath2 = './DATA_TXT/RUN010_E5.txt'
#
# data1 = np.loadtxt(filepath1, skiprows=1)
# data2 = np.loadtxt(filepath2, skiprows=1)
#
# data1_x = data1[:, 0]
# data1_y = data1[:, 1]
#
# data2_x = data2[:, 0]
# data2_y = data2[:, 1]


# Create a 2D histogram with indices corresponding to data1_x and data2_x
hist, xedges, yedges = np.histogram2d(data1_x, data2_x, bins=[3, 3], range=[[1, 3], [1, 3]])

# Calculate the sum of data1_y and data2_y for each bin
sum_values = np.zeros_like(hist)
for i in range(len(xedges)-1):
    for j in range(len(yedges)-1):
        xmin, xmax = xedges[i], xedges[i+1]
        ymin, ymax = yedges[j], yedges[j+1]
        xindices = np.where((data1_x >= xmin) & (data1_x < xmax))[0]
        yindices = np.where((data2_x >= ymin) & (data2_x < ymax))[0]
        np.add.at(sum_values, (i, j), np.sum(data1_y[xindices]) + np.sum(data2_y[yindices]))

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create the 2D histogram with the sums as the color argument
sc = ax.hist2d(xedges[:-1], yedges[:-1], bins=[3, 3], weights=sum_values.flatten(), cmap='cool', alpha=0.8)

# Add color bar
plt.colorbar(sc[3], label='Sum of data1_y and data2_y')

# Set labels for x and y axes
plt.xlabel('data1_x')
plt.ylabel('data2_x')

# Show the plot
plt.show()