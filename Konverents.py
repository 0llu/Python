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

        # Tekstiväljad ja sildid osalejate lisamiseks
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.organization_label = tk.Label(master, text="Organization:")
        self.organization_label.grid(row=1, column=0, sticky="e")
        self.organization_entry = tk.Entry(master)
        self.organization_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=3, column=0, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=3, column=1)

        self.presentation_label = tk.Label(master, text="Presentation Title:")
        self.presentation_label.grid(row=4, column=0, sticky="e")
        self.presentation_entry = tk.Entry(master)
        self.presentation_entry.grid(row=4, column=1)

        # Nupp osaleja lisamiseks
        self.register_button = tk.Button(master, text="Register", command=self.register_participant)
        self.register_button.grid(row=5, column=1, sticky="e")

        # Nupp osalejate kuvamiseks
        self.view_button = tk.Button(master, text="View Participants", command=self.view_participants_window)
        self.view_button.grid(row=6, column=1, sticky="e")

        # Lae osalejate andmed
        self.load_participants()

    def register_participant(self):
        name = self.name_entry.get()
        organization = self.organization_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        presentation = self.presentation_entry.get()

        if name and email:
            # Genereeri unikaalne ID
            participant_id = self.generate_id()

            # Lisame osaleja andmed
            participant_data = {'ID': participant_id, 'Name': name, 'Organization': organization, 'Email': email,
                                'Phone': phone, 'Presentation Title': presentation}
            self.participants.append(participant_data)

            # Puhasta väljad pärast registreerimist
            self.clear_fields()

            messagebox.showinfo("Success", "Participant registered successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and email.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.organization_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.presentation_entry.delete(0, tk.END)

    def generate_id(self):
        # Genereeri unikaalne ID pikkusega 8 tähemärki
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def load_participants(self):
        try:
            with open('participants.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.participants.append(row)
        except FileNotFoundError:
            pass

    def view_participants_window(self):
        participants_window = tk.Toplevel(self.master)
        participants_window.title("View Participants")

        search_label = tk.Label(participants_window, text="Search:")
        search_label.grid(row=0, column=0, sticky="e")
        self.search_entry = tk.Entry(participants_window)
        self.search_entry.grid(row=0, column=1)

        search_button = tk.Button(participants_window, text="Search", command=self.search_participants)
        search_button.grid(row=0, column=2)

        self.participant_text = tk.Text(participants_window, height=10, width=50)
        self.participant_text.grid(row=1, columnspan=3)

        for participant in self.participants:
            self.participant_text.insert(tk.END, f"ID: {participant['ID']}\nName: {participant['Name']}\nOrganization: {participant['Organization']}\nEmail: {participant['Email']}\nPhone: {participant['Phone']}\nPresentation Title: {participant['Presentation Title']}\n\n")

        save_button = tk.Button(participants_window, text="Save Changes", command=self.save_changes)
        save_button.grid(row=2, column=1)

    def search_participants(self):
        self.participant_text.delete(1.0, tk.END)
        search_query = self.search_entry.get().lower()
        if search_query:
            for participant in self.participants:
                for key, value in participant.items():
                    if search_query in value.lower() and key != 'ID':
                        self.participant_text.insert(tk.END, f"{key}: {value}\n")

    def save_changes(self):
        new_participants = []
        for line in self.participant_text.get("1.0", tk.END).strip().split("\n\n"):
            participant_data = {}
            for item in line.strip().split("\n"):
                key, value = item.split(": ")
                participant_data[key] = value
            new_participants.append(participant_data)

        try:
            with open('participants.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Name', 'Organization', 'Email', 'Phone', 'Presentation Title']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for participant in new_participants:
                    writer.writerow(participant)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Success", "Changes saved successfully!")

def main():
    root = tk.Tk()
    app = ConferenceRegistrationSystem(root)
    root.mainloop()

if __name__ == "__main__":

    main()