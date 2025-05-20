import tkinter as tk
from tkinter import ttk
from data_handler import DataHandler
from visualizer import Visualizer
from export_tools import ExportTools

class StatistikVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Statistik Visualizer")
        self.root.geometry("800x600")

        self.data_handler = DataHandler()
        self.visualizer = Visualizer()
        self.export_tools = ExportTools()

        self.setup_ui()

    def setup_ui(self):
        # Entry
        self.entry_label = ttk.Label(self.root, text="Masukkan data (pisah dengan koma):")
        self.entry_label.pack(pady=5)

        self.data_entry = ttk.Entry(self.root, width=80)
        self.data_entry.pack(pady=5)

        self.submit_btn = ttk.Button(self.root, text="Proses Data", command=self.process_data)
        self.submit_btn.pack(pady=10)

        # Statistik output
        self.output_text = tk.Text(self.root, height=10)
        self.output_text.pack(pady=5, fill=tk.X, padx=10)

        # Tombol visualisasi
        self.hist_btn = ttk.Button(self.root, text="Tampilkan Histogram", command=self.show_histogram)
        self.hist_btn.pack(pady=5)

        self.box_btn = ttk.Button(self.root, text="Tampilkan Boxplot", command=self.show_boxplot)
        self.box_btn.pack(pady=5)

        self.export_btn = ttk.Button(self.root, text="Ekspor Laporan ke TXT", command=self.export_report)
        self.export_btn.pack(pady=10)

    def process_data(self):
        raw_data = self.data_entry.get()
        self.data_handler.load_from_string(raw_data)
        stats = self.data_handler.calculate_statistics()

        self.output_text.delete("1.0", tk.END)
        for key, val in stats.items():
            self.output_text.insert(tk.END, f"{key}: {val}\n")

    def show_histogram(self):
        self.visualizer.show_histogram(self.data_handler.data)

    def show_boxplot(self):
        self.visualizer.show_boxplot(self.data_handler.data)

    def export_report(self):
        stats = self.data_handler.calculate_statistics()
        self.export_tools.export_to_txt(stats)

if __name__ == '__main__':
    root = tk.Tk()
    app = StatistikVisualizerApp(root)
    root.mainloop()
