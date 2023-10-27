import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

def search_text():
    search_text = search_entry.get()
    text_content = text.get("1.0", tk.END)
    search_result = text_content.lower().count(search_text.lower())
    messagebox.showinfo("Search Result", f"'{search_text}' found {search_result} times.")

app = tk.Tk()
app.title("Minimalistic Text Editor")

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

search_label = tk.Label(app, text="Search Text:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()
search_button = tk.Button(app, text="Search", command=search_text)
search_button.pack()

text = tk.Text(app)
text.pack()

app.mainloop()
