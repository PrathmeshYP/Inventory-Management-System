import tkinter as tk
from database import connect_db
from product import product_window
from supplier import supplier_window
from stock import stock_window
from view_stock import view_stock_window
import theme

connect_db()

root = tk.Tk()
root.geometry("620x470")
root.title("Inventory Management System")

def apply_theme():
    t = theme.current_theme
    root.config(bg=t["bg"])
    title.config(bg=t["bg"], fg=t["primary"])
    card.config(bg=t["card"])

    for btn in buttons:
        btn.config(bg=t["primary"], fg="white")

def toggle():
    theme.toggle_theme()
    apply_theme()

# -------- TITLE --------
title = tk.Label(
    root,
    text="Inventory Management System",
    font=("Segoe UI", 20, "bold")
)
title.pack(pady=20)

# -------- TOGGLE BUTTON --------
toggle_btn = tk.Button(
    root,
    text="🌙 / ☀ ",
    command=toggle,
    font=("Segoe UI", 10, "bold"),
    bd=0
)
toggle_btn.pack(pady=5)

# -------- CARD --------
card = tk.Frame(root)
card.pack(padx=40, pady=15, fill="both", expand=True)

buttons = []

def add_btn(text, cmd):
    b = tk.Button(
        card,
        text=text,
        command=cmd,
        font=("Segoe UI", 12, "bold"),
        bd=0,
        pady=10,
        cursor="hand2"
    )
    b.pack(fill="x", pady=8)
    buttons.append(b)

add_btn("📦 Product Management", product_window)
add_btn("🏭 Supplier Management", supplier_window)
add_btn("📊 Stock Management", stock_window)
add_btn("📋 View Available Stock", view_stock_window)
add_btn("❌ Exit", root.destroy)

apply_theme()
root.mainloop()
