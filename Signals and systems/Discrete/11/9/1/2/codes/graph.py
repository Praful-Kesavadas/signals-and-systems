import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

# Enable LaTeX rendering in matplotlib
rc('text', usetex=True)

# Define the function
def func(n):
    return n / (n + 1)

# Generate integer values for n
n_values = np.arange(0, 11, 1)

# Calculate corresponding y values
y_values = func(n_values)

# Plot the graph
plt.stem(n_values, y_values, label=r'$\frac{n}{n+1}$', basefmt='b')

# Set labels and title
plt.xlabel(r'$n$')
plt.ylabel(r'$\frac{n}{n+1}$')
plt.title(r'Graph of $\frac{n}{n+1}$')

# Add a legend
#plt.legend()
plt.savefig('graph.png')
# Show the plot
#plt.show()

