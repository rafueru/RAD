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

        # Repita para outros campos...

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data_to_backend)
        self.submit_button.pack()

    def submit_data_to_backend(self):
        data = {
            "name": self.name_entry.get(),
            # Adicione outros campos conforme necessário
        }
        response = requests.post('http://localhost:5000/submit', json=data)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Data submitted!")
        else:
            messagebox.showerror("Error", "Failed to submit data!")

class ManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manager Interface")
        self.get_developers_button = tk.Button(self, text="Get Developers", command=self.get_developers_from_backend)
        self.get_developers_button.pack()

    def get_developers_from_backend(self):
        response = requests.get('http://localhost:5000/get_developers')
        if response.status_code == 200:
            developers = response.json()['developers']
            for developer in developers:
                tk.Label(self, text=f"Name: {developer[0]}, City: {developer[2]}").pack()  # Ajuste conforme necessário

if __name__ == '__main__':
    app_choice = input("Digite '1' para lançar a interface do desenvolvedor ou '2' para lançar a interface do gerente: ")
    if app_choice == '1':
        developer_app = DeveloperApp()
        developer_app.mainloop()
    elif app_choice == '2':
        manager_app = ManagerApp()
        manager_app.mainloop()
