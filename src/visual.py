import matplotlib
import matplotlib.pyplot as plot
import seaborn as sea

def incidents_plot(count):
    """
    Creates a bar plot of workplace incident count by type
    """

    sea.set(style="whitegrid")
    plot.figure(figsize=(10,6))

    # Create the plot and capture the axis
    ax = sea.barplot(x=count.index, y=count.values, palette="plasma")

    # Apply log scale if needed
    ax.set_yscale("log")

    # Add count values on top of each bar
    for i, value in enumerate(count.values):
        ax.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

    ax.set_xlabel("Incident Type")
    ax.set_ylabel("Count (log scale)")
    ax.set_title("Workplace incidents by type")

    plot.tight_layout()
    plot.show()