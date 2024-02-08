import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# title and labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# tick labels
ax.tick_params(labelsize=14)

# range for the axises(?)
ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain") <- can override the notation
# (doesnt look good with larger numbers)

# opens a window showing the plot
# plt.show()

# saves plot to file
plt.savefig("squares_plot.png", bbox_inches="tight")
