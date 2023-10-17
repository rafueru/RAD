import tkinter as tk
from tkinter import messagebox

def submit_data():
    # Aqui, você faria uma requisição ao back-end para enviar os dados.
    # Por simplicidade, estou apenas mostrando uma mensagem.
    messagebox.showinfo("Info", "Data submitted!")

app = tk.Tk()
app.title("Developer Submission")

name_label = tk.Label(app, text="Name")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

# Repita para outros campos...

submit_button = tk.Button(app, text="Submit", command=submit_data)
submit_button.pack()

app.mainloop()

