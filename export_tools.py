from tkinter import filedialog

class ExportTools:
    def export_to_txt(self, stats_dict):
        if not stats_dict:
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for key, val in stats_dict.items():
                    f.write(f"{key}: {val}\n")
