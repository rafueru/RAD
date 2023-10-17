import tkinter as tk
from tkinter import messagebox
import requests

def submit_data_to_backend():
    data = {
        "name": name_entry.get(),
        # Adicione outros campos conforme necessário
    }
    response = requests.post('http://backend:5000/submit', json=data)
    if response.status_code == 200:
        messagebox.showinfo("Info", "Data submitted!")
    else:
        messagebox.showerror("Error", "Failed to submit data!")

app = tk.Tk()
app.title("Developer Submission")

name_label = tk.Label(app, text="Name")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

# Repita para outros campos...

submit_button = tk.Button(app, text="Submit", command=submit_data_to_backend)
submit_button.pack()

app.mainloop()
