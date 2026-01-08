import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

import requests
from utils.config import UPLOAD_FLAG_FILE
from utils import messagebox
from api_client import get_plots


def open_upload_plot_excel(dashboard_root):
    window = tk.Toplevel(dashboard_root)
    window.title("Upload Plot Excel")
    window.geometry("420x300")
    window.resizable(False, False)

    # 🔒 Disable dashboard
    dashboard_root.attributes("-disabled", True)

    def on_close():
        dashboard_root.attributes("-disabled", False)
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(
        window,
        text="Upload Plot Details (Excel)",
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    progress = ttk.Progressbar(
        window,
        orient="horizontal",
        length=300,
        mode="determinate"
    )
    progress.pack(pady=10)

    status_label = tk.Label(window, text="")
    status_label.pack(pady=5)

    tk.Button(
        window,
        text="Select Excel File",
        width=25,
        command=lambda: upload_plot_excel(window, progress, status_label)
    ).pack(pady=10)

    tk.Button(
        window,
        text="Close",
        command=on_close
    ).pack(pady=10)


def upload_plot_excel(window, progress, status_label):
    if os.path.exists(UPLOAD_FLAG_FILE):
        messagebox.showinfo("Info", "Plot details already uploaded.")
        return

    file_path = filedialog.askopenfilename(
        parent=window,
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )

    if not file_path:
        return

    try:
        df = pd.read_excel(file_path)

        required_cols = [
            "plot_number",
            "total_area",
            "market_value",
            "min_sell_value"
        ]

        for col in required_cols:
            if col not in df.columns:
                messagebox.showerror("Error", f"Missing column: {col}")
                return

        # 🔁 Get existing plot numbers (skip duplicates)
        existing_numbers = {
            p["plot_number"] for p in get_plots()
        }

        total_rows = len(df)
        progress["maximum"] = total_rows
        progress["value"] = 0

        uploaded = 0
        skipped = 0

        for index, row in df.iterrows():
            plot_number = str(row["plot_number"]).strip()

            # ❌ Skip duplicate plot numbers
            if plot_number in existing_numbers:
                skipped += 1
                progress["value"] += 1
                status_label.config(
                    text=f"Skipped duplicate: {plot_number}"
                )
                window.update_idletasks()
                continue

            # 🧪 Validate numeric fields
            try:
                total_area = float(row["total_area"])
                market_value = float(row["market_value"])
                min_sell_value = float(row["min_sell_value"])

                if total_area <= 0 or market_value <= 0 or min_sell_value <= 0:
                    raise ValueError
            except Exception:
                messagebox.showerror(
                    "Invalid Data",
                    f"Invalid numeric value at Excel row {index + 2}"
                )
                return

            payload = {
                "plot_number": plot_number,
                "total_area": total_area,
                "market_value": market_value,
                "min_sell_value": min_sell_value,
            }

            res = requests.post(
                f"{BASE_API_URL}/plots/",
                json=payload
            )
            res.raise_for_status()

            uploaded += 1
            progress["value"] += 1
            status_label.config(
                text=f"Uploaded {uploaded + skipped}/{total_rows}"
            )
            window.update_idletasks()

        with open(UPLOAD_FLAG_FILE, "w") as f:
            f.write("uploaded")

        messagebox.showinfo(
            "Upload Complete",
            f"Uploaded: {uploaded}\nSkipped (duplicates): {skipped}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Upload failed:\n{e}")
