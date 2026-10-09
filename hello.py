import tkinter as tk
from tkinter import simpledialog

BLUE = "#1e5bd8"


def show_blue_message(title, text):
    box = tk.Toplevel(root)
    box.title(title)
    box.configure(bg=BLUE, padx=20, pady=20)
    box.resizable(False, False)

    tk.Label(box, text=text, bg=BLUE, fg="white", font=("Segoe UI", 12)).pack(pady=(0, 15))
    tk.Button(box, text="OK", width=10, command=box.destroy).pack()

    box.grab_set()
    root.wait_window(box)


root = tk.Tk()
root.withdraw()

message = simpledialog.askstring("Hello", "What would you like to say?")

if message:
    print(message)
    show_blue_message("You said", message)

root.destroy()
