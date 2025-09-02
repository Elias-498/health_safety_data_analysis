import matplotlib
import matplotlib.pyplot as plot
import seaborn as sea

def incidents_plot(count):
    """
    Creates a bar plot of workplace incident count by type
    """

    sea.set(style="whitegrid")
    plot.figure(figsize=(10,10))
    sea.barplot(x=count.index, y=count.values, palette="magma")
    
    plot.xlabel("Incident Type")
    plot.ylabel("Count")
    plot.title("Workplace incidents by type")

    plot.show()