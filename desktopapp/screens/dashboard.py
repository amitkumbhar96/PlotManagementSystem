import tkinter as tk
from api_client import get_plots
from screens.plot_details import open_plot_details
from screens.upload_plot_excel import open_upload_plot_excel


def open_dashboard():
    root = tk.Tk()
    root.title("Plot Dashboard")
    root.geometry("700x450")

    # 🔹 Upload button
    top_frame = tk.Frame(root)
    top_frame.pack(fill="x", padx=10, pady=5)

    tk.Button(
        top_frame,
        text="Upload Plot Excel",
        bg="#2c7be5",
        fg="white",
        command=open_upload_plot_excel(root)
    ).pack(side="right")

    plots = get_plots()

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    for i, plot in enumerate(plots):
        color = "green" if plot["status"] == "AVAILABLE" else "red"

        btn = tk.Button(
            frame,
            text=f"Plot {plot['plot_number']}",
            bg=color,
            fg="white",
            width=14,
            height=2,
            command=lambda p=plot: open_plot_details(p)
        )
        btn.grid(row=i // 5, column=i % 5, padx=6, pady=6)

    root.mainloop()
