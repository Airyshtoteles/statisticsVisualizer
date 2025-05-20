import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def show_histogram(self, data):
        if data.empty:
            return
        plt.figure(figsize=(8, 4))
        sns.histplot(data, bins=10, kde=True)
        plt.title("Histogram Data")
        plt.xlabel("Nilai")
        plt.ylabel("Frekuensi")
        plt.tight_layout()
        plt.show()

    def show_boxplot(self, data):
        if data.empty:
            return
        plt.figure(figsize=(6, 2))
        sns.boxplot(x=data)
        plt.title("Boxplot Data")
        plt.tight_layout()
        plt.show()
