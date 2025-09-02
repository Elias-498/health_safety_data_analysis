import matplotlib
import matplotlib.pyplot as plot
import seaborn as sea

def incidents_plot(count):

    sea.set(style="whitegrid")

    plot.figure(figsize=(10,10))

    sea.barplot(x=count.index, y=count.values, palette="magma", hue=None)

    plot.xlabel("Incident Type")
    plot.ylabel("Count")
    plot.title("Workplace incidents by type")

    plot.show()