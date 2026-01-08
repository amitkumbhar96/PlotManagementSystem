# screens/inquiry_form.py
import tkinter as tk
from api_client import inquiry_plot
from utils.messagebox import info

def open_inquiry_form(plot):
    win = tk.Toplevel()
    win.title("Inquiry")

    fields = {}

    for lbl in ["Name", "Mobile", "Email"]:
        tk.Label(win, text=lbl).pack()
        e = tk.Entry(win)
        e.pack()
        fields[lbl] = e

    def submit():
        data = {
            "plot_id": plot["id"],
            "name": fields["Name"].get(),
            "mobile": fields["Mobile"].get(),
            "email": fields["Email"].get()
        }
        inquiry_plot(data)
        info("Inquiry Saved")
        win.destroy()

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
