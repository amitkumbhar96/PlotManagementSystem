# utils/messagebox.py
from tkinter import messagebox

def info(msg):
    messagebox.showinfo("Info", msg)

def error(msg):
    messagebox.showerror("Error", msg)
