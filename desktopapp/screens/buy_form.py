# screens/buy_form.py
import tkinter as tk
from api_client import buy_plot
from utils.messagebox import info

def open_buy_form(plot):
    win = tk.Toplevel()
    win.title("Buy Plot")

    fields = {}

    labels = [
        "Name",
        "Mobile",
        "Email",
        "Booking Amount",
        "Sell Value"
    ]

    for lbl in labels:
        tk.Label(win, text=lbl).pack()
        e = tk.Entry(win)
        e.pack()
        fields[lbl] = e

    def submit():
        data = {
            "plot_id": plot["id"],
            "name": fields["Name"].get(),
            "mobile": fields["Mobile"].get(),
            "email": fields["Email"].get(),
            "booking_amount": fields["Booking Amount"].get(),
            "sell_value": fields["Sell Value"].get()
        }
        buy_plot(data)
        info("Plot Sold Successfully")
        win.destroy()

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
