import pandas as pd
import numpy as np

class DataHandler:
    def __init__(self):
        self.data = []

    def load_from_string(self, data_str):
        try:
            data = [float(x) for x in data_str.split(',') if x.strip() != '']
            self.data = pd.Series(data)
        except ValueError:
            self.data = pd.Series([])

    def calculate_statistics(self):
        if self.data.empty:
            return {"Error": "Data kosong atau format salah."}

        stats = {
            "Jumlah Data": self.data.count(),
            "Mean": self.data.mean(),
            "Median": self.data.median(),
            "Modus": self.data.mode().values.tolist(),
            "Standar Deviasi": self.data.std(),
            "Varians": self.data.var(),
            "Nilai Maksimum": self.data.max(),
            "Nilai Minimum": self.data.min(),
            "Range": self.data.max() - self.data.min()
        }
        return stats
