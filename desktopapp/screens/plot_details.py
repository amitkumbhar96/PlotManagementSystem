# screens/plot_details.py
import tkinter as tk
from screens.buy_form import open_buy_form
from screens.inquiry_form import open_inquiry_form

def open_plot_details(plot):
    win = tk.Toplevel()
    win.title(f"Plot {plot['plot_number']}")
    win.geometry("350x400")

    for k, v in plot.items():
        tk.Label(win, text=f"{k}: {v}", anchor="w").pack(fill="x")

    tk.Button(
        win,
        text="Buy",
        bg="green",
        fg="white",
        command=lambda: open_buy_form(plot)
    ).pack(pady=8)

    tk.Button(
        win,
        text="Inquiry",
        bg="blue",
        fg="white",
        command=lambda: open_inquiry_form(plot)
    ).pack(pady=8)
