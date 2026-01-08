# screens/login_screen.py
import tkinter as tk
from api_client import login
from auth_store import set_token
from utils.messagebox import error
from screens.dashboard import open_dashboard

def open_login():
    root = tk.Tk()
    root.title("Admin Login")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack()
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    def do_login():
        try:
            res = login(username.get(), password.get())
            set_token(res["access_token"])
            root.destroy()
            open_dashboard()
        except Exception as e:
            error(str(e))

    tk.Button(root, text="Login", command=do_login).pack(pady=10)
    root.mainloop()
