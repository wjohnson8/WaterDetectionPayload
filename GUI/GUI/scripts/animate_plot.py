import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Replace with your CSV filename
csv_filename = '/Users/lola/Desktop/CU/CAPSTONE23-24/WaterDetectionPayload/WaterDetectionPayload/DATA_PROCESSING/data/LED_spectrum_data/1050_spectrum.csv'

# Load the data from the CSV file
data = pd.read_csv(csv_filename)

# Prepare the figure for plotting
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Setting the axes limits
ax.set_xlim(data.iloc[:, 1].min(), data.iloc[:, 1].max())
ax.set_ylim(data.iloc[:, 0].min(), data.iloc[:, 0].max())

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(i):
    x = data.iloc[:i, 1]  # Second column for X-axis
    y = data.iloc[:i, 0]  # First column for Y-axis
    line.set_data(x, y)
    return line,

# Call the animator
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(data), interval=50, blit=True)

# Show the plot
plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import pandas as pd
# import sys

# # Filenames of the CSV files
# #csv_filenames = ['/Users/lola/Desktop/CU/CAPSTONE23-24/WaterDetectionPayload/WaterDetectionPayload/DATA_PROCESSING/data/LED_spectrum_data/1050_spectrum.csv', '/Users/lola/Desktop/CU/CAPSTONE23-24/WaterDetectionPayload/WaterDetectionPayload/DATA_PROCESSING/data/LED_spectrum_data/1200_spectrum.csv', '/Users/lola/Desktop/CU/CAPSTONE23-24/WaterDetectionPayload/WaterDetectionPayload/DATA_PROCESSING/data/LED_spectrum_data/1550_spectrum.csv']
# csv_filenames = ['/Users/lola/Desktop/CU/CAPSTONE23-24/WaterDetectionPayload/WaterDetectionPayload/DATA_PROCESSING/data/LED_spectrum_data/all_LEDs_spectrum.csv']

# # Load and concatenate the data from the CSV files
# dataframes = [pd.read_csv(filename) for filename in csv_filenames]
# data = pd.concat(dataframes, ignore_index=True)

# ice_data = pd.read_csv('/Users/lola/Desktop/CU/CAPSTONE23-24/EXPERIMENT_OP_20201223_001/refl-VNIR_H2O_ice_70micron_70K/refl-VNIR_H2O_ice_70micron_70K_abg.data.csv')

# # Prepare the figure for plotting
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)

# # Setting the axes limits
# #ax.set_xlim(data.iloc[:, 1].min(), data.iloc[:, 1].max())
# ax.set_xlim(850, 1800)
# ax.set_ylim(data.iloc[:, 0].min(), data.iloc[:, 0].max())

# # Initialization function for animation
# def init():
#     line.set_data([], [])
#     return line,

# # Animation function
# def animate(i):
#     x = data.iloc[:i, 1]  # X-axis data from the second column
#     y = data.iloc[:i, 0]  # Y-axis data from the first column
#     line.set_data(x, y)
#     return line,

# # Check for command-line argument for animation
# animate_plot = len(sys.argv) > 1 and sys.argv[1] == 'animate'

# if animate_plot:
#     # Call the animator
#     ani = animation.FuncAnimation(fig, animate, init_func=init,
#                                   frames=len(data), interval=50, blit=True)
# else:
#     # Plot without animation
#     ax.plot(data.iloc[:, 1], data.iloc[:, 0], color='red', label='LEDs specs')
#     # Plot the ice data
#     ax.plot(ice_data['wavelength(nm)'], ice_data['reflectance_factor'], color='blue', label='Ice Data')

# # Show the plot
# plt.show()
