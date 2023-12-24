from tkinter import *
from tkinter import ttk
from datetime import datetime

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To Do Application")

        # Use a themed style
        style = ttk.Style()
        style.theme_use("clam")

        # Apply a themed background color to the main window
        style.configure("TFrame", background="#E0E0E0")

        self.frame = ttk.Frame(self.master, padding=(10, 10, 10, 10), style="TFrame")
        self.frame.pack(pady=20)

        self.listbox = Listbox(self.frame, width=30, height=10, bd=1, relief=SOLID, highlightthickness=0)
        self.listbox.pack(padx=20, pady=20, side=LEFT, fill=BOTH, expand=True)

        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar_y.pack(pady=20, side=RIGHT, fill=Y)

        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scrollbar_x.pack(padx=20, side=BOTTOM, fill=X)

        self.scrollbar_y.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar_x.set)

        self.entry = ttk.Entry(self.master, width=30, font=("Helvetica", 10))
        self.entry.pack(pady=10)

        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(pady=20)

        style.configure("TButton", padding=(8, 4, 8, 4), font=("Helvetica", 10))

        self.add_button = ttk.Button(self.button_frame, text="Add Task", width=10, command=self.add_task)
        self.add_button.pack(padx=10, pady=10, side=LEFT)

        self.remove_button = ttk.Button(self.button_frame, text="Remove Task", width=10, command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10, side=LEFT)

        self.edit_button = ttk.Button(self.button_frame, text="Edit Task", width=10, command=self.edit_task)
        self.edit_button.pack(padx=10, pady=10, side=LEFT)

        self.clear_button = ttk.Button(self.button_frame, text="Clear All", width=10, command=self.clear_tasks)
        self.clear_button.pack(padx=10, pady=10, side=LEFT)

        style.configure("TLabel", font=("Helvetica", 10, "bold"), background="#E0E0E0")

        self.datetime_label = ttk.Label(self.master, text="", style="TLabel")
        self.datetime_label.pack()

        self.update_datetime()
        self.master.after(1000, self.update_datetime)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            self.listbox.delete(selected_task)

    def edit_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            current_task = self.listbox.get(selected_task)
            self.entry.delete(0, END)
            self.entry.insert(0, current_task)

    def clear_tasks(self):
        self.listbox.delete(0, END)

    def update_datetime(self):
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%I:%M:%S %p")
        current_day = now.strftime("%A")

        datetime_str = f"Date: {current_date} | Time: {current_time} | Day: {current_day}"
        self.datetime_label.config(text=datetime_str)

        self.master.after(1000, self.update_datetime)

if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()
