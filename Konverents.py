import tkinter as tk
from tkinter import messagebox
import csv
import random
import string

class ConferenceRegistrationSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Conference Registration System")

        # Andmestruktuur osalejate salvestamiseks
        self.participants = []

        # Andmestruktuur osalejate ID-de hoidmiseks, et tagada unikaalsus
        self.participant_ids = set()

        # Laadi andmed
        self.load_data()

        # Tekstiväljad ja siltide loomine
        self.name_label = tk.Label(master, text="Nimi:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.organization_label = tk.Label(master, text="Asutus:")
        self.organization_label.grid(row=1, column=0, sticky="e")
        self.organization_entry = tk.Entry(master)
        self.organization_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.phone_label = tk.Label(master, text="Telefon:")
        self.phone_label.grid(row=3, column=0, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=3, column=1)

        self.presentation_label = tk.Label(master, text="Esitluse Pealkiri:")
        self.presentation_label.grid(row=4, column=0, sticky="e")
        self.presentation_entry = tk.Entry(master)
        self.presentation_entry.grid(row=4, column=1)

        # Nuppude loomine
        self.register_button = tk.Button(master, text="Registeeri", command=self.register_participant)
        self.register_button.grid(row=5, column=1, sticky="e")

        self.view_button = tk.Button(master, text="Vaata Osalejaid", command=self.view_participants)
        self.view_button.grid(row=6, column=1, sticky="e")

        # Salvestamise nupp
        self.save_button = tk.Button(master, text="Salvesta Andmed", command=self.save_data)
        self.save_button.grid(row=7, column=1, sticky="e")

    def register_participant(self):
        name = self.name_entry.get()
        organization = self.organization_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        presentation = self.presentation_entry.get()

        if name and email:
            # Genereeri unikaalne ID
            participant_id = self.generate_id()
            while participant_id in self.participant_ids:
                participant_id = self.generate_id()

            # Lisame osaleja andmed
            participant_data = {'ID': participant_id, 'Name': name, 'Organization': organization, 'Email': email,
                                'Phone': phone, 'Presentation Title': presentation}
            self.participants.append(participant_data)
            self.participant_ids.add(participant_id)

            # Puhasta väljad pärast registreerimist
            self.clear_fields()

            messagebox.showinfo("Success", "Participant registered successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and email.")

    def view_participants(self):
        if self.participants:
            view_window = tk.Toplevel(self.master)
            view_window.title("View Participants")
            text = tk.Text(view_window)
            text.pack()

            for participant in self.participants:
                text.insert(tk.END, f"ID: {participant['ID']}\nName: {participant['Name']}\nOrganization: {participant['Organization']}\nEmail: {participant['Email']}\nPhone: {participant['Phone']}\nPresentation Title: {participant['Presentation Title']}\n\n")
        else:
            messagebox.showinfo("Info", "No participants registered yet.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.organization_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.presentation_entry.delete(0, tk.END)

    def generate_id(self):
        # Genereeri unikaalne ID pikkusega 8 tähemärki
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def load_data(self):
        try:
            # Lae andmed failist, kui see olemas
            with open('participants.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.participants.append(row)
                    self.participant_ids.add(row['ID'])
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('participants.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ID', 'Name', 'Organization', 'Email', 'Phone', 'Presentation Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for participant in self.participants:
                writer.writerow(participant)

def main():
    root = tk.Tk()
    app = ConferenceRegistrationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()


