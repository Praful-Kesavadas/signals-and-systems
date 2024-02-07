import matplotlib.pyplot as plt
import numpy as np

# Read the sequence from the file
with open("sequence.txt", "r") as file:
    sequence = [float(line.strip()) for line in file]

# Plot the sequence
sequence_array= np.array(sequence)

# Add labels and title
plt.stem(range(len(sequence_array)), sequence_array, basefmt="k-", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(range(len(sequence_array)))
#plt.title('Sequence Plot: n/(n+1)')

# Save the graph as graph1.png
plt.savefig('graph1.png')

# Show the plot
plt.show()

