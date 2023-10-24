import tkinter as tk
from tkinter import messagebox
import requests

class DeveloperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Developer Submission")

        self.name_label = tk.Label(self, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.age_label = tk.Label(self, text="Age")  # Adicionando label para idade
        self.age_label.pack()
        self.age_entry = tk.Entry(self)  # Adicionando entrada para idade
        self.age_entry.pack()

        # Repita para outros campos...

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data_to_backend)
        self.submit_button.pack()

    def submit_data_to_backend(self):
        data = {
            "name": self.name_entry.get(),
            "age": self.age_entry.get(),  # Incluindo idade no dicionário data
            # Adicione outros campos conforme necessário
        }
        response = requests.post('http://localhost:5000/submit', json=data)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Data submitted!")
        else:
            messagebox.showerror("Error", "Failed to submit data!")

if __name__ == '__main__':
    developer_app = DeveloperApp()
    developer_app.mainloop()
