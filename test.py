import matplotlib.pyplot as plt
import numpy as np

data1_x = [1.5, 2.5, 3.5]
data1_y = [1, 5, 2]
data2_x = [1.5, 2.5, 3.5]
data2_y = [5, 3, 0]

# Part 1
# # Initialize lists to store the calculated sums
# sum_values = []
#
# # Calculate the sum of data1_y and data2_y for each combination of data1_x and data2_x
# sum_values = []
# for x1, y1 in zip(data1_x, data1_y):
#     for x2, y2 in zip(data2_x, data2_y):
#         sum_values.append(y1 + y2)
#
# # Create a figure and a set of subplots
# fig, ax = plt.subplots()
#
# # Plot the histogram with color mapping based on the sum of values
# sc = ax.scatter([x1 for x1 in data1_x for _ in data2_x],
#                 [x2 for _ in data1_x for x2 in data2_x],
#                 c=sum_values, cmap='cool', s=100, alpha=0.8)
#
# # Add color bar
# plt.colorbar(sc, label='Sum of data1_y and data2_y')
#
# # Set labels for x and y axes
# plt.xlabel('data1_x')
# plt.ylabel('data2_x')
#
# # Show the plot
# plt.show()


# Part 2
# Create a 2D histogram with 4x4 bins
hist, xedges, yedges = np.histogram2d(data1_x, data2_x, bins=[3, 3], range=[[1, 4], [1, 4]])

# Calculate the sum of data1_y and data2_y for each bin
sum_values = []
for i in range(len(hist)):
    for j in range(len(hist[i])):
        xmin, xmax = xedges[i], xedges[i+1]
        ymin, ymax = yedges[j], yedges[j+1]
        xindices = np.where((data1_x >= xmin) & (data1_x < xmax))[0]
        yindices = np.where((data2_x >= ymin) & (data2_x < ymax))[0]
        sum_values = np.sum(data1_y[xindices]) + np.sum(data2_y[yindices])

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create the 2D histogram with the sums as the color argument
sc = ax.hist2d(xedges[:-1], yedges[:-1], bins=[4, 4], weights=sum_values.flatten(), cmap='cool', alpha=0.8)

# Add color bar
plt.colorbar(sc[3], label='Sum of data1_y and data2_y')

# Set labels for x and y axes
plt.xlabel('data1_x')
plt.ylabel('data2_x')

# Show the plot
plt.show()



# import os, sys
# import ROOT
# import pandas as pd
#
# # Загрузка данных из txt файлов
# de2 = pd.read_csv('DATA_TXT/RUN010_dE2.txt', sep='\s+', header=None)
# e5 = pd.read_csv('DATA_TXT/RUN010_E5.txt', sep='\s+', header=None)
#
# # Создание гистограммы
# h = ROOT.TH1F('h', 'h', 100, 0, 100)
#
# # Заполнение гистограммы данными
# for i in range(len(de2)):
#     h.Fill(de2.iloc[i][0], e5.iloc[i][0])
#
# # Отрисовка гистограммы
# c = ROOT.TCanvas('c', 'c')
# h.Draw()
