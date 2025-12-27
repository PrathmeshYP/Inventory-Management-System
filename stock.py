import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
from datetime import datetime
import theme

def stock_window():
    conn = connect_db()
    cur = conn.cursor()
    t = theme.current_theme

    win = tk.Toplevel()
    win.geometry("450x420")
    win.title("Stock Management")
    win.config(bg=t["bg"])

    tk.Label(
        win,
        text="Stock Management",
        font=("Segoe UI", 16, "bold"),
        bg=t["bg"],
        fg=t["primary"]
    ).pack(pady=20)

    card = tk.Frame(win, bg=t["card"])
    card.pack(padx=30, pady=10, fill="both", expand=True)

    # ---------- PRODUCT DROPDOWN ----------
    tk.Label(card, text="Select Product",
             bg=t["card"], fg=t["text"],
             font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10, 0))

    product_var = tk.StringVar()
    product_combo = ttk.Combobox(card, textvariable=product_var, state="readonly")
    product_combo.pack(padx=20, fill="x")

    # Load products
    cur.execute("SELECT product_id, name FROM products")
    products = cur.fetchall()

    product_map = {name: pid for pid, name in products}
    product_combo["values"] = list(product_map.keys())

    # ---------- QUANTITY ----------
    tk.Label(card, text="Quantity",
             bg=t["card"], fg=t["text"],
             font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10, 0))

    qty_entry = tk.Entry(card, font=("Segoe UI", 11))
    qty_entry.pack(padx=20, fill="x")

    # ---------- FUNCTIONS ----------
    def stock_in():
        if product_var.get() == "" or qty_entry.get() == "":
            messagebox.showerror("Error", "Please select product and enter quantity")
            return

        qty = int(qty_entry.get())
        pid = product_map[product_var.get()]

        cur.execute(
            "UPDATE products SET quantity = quantity + ? WHERE product_id = ?",
            (qty, pid)
        )

        cur.execute(
            "INSERT INTO stock_logs VALUES (NULL,?,?,?,?)",
            (pid, "IN", qty, datetime.now())
        )

        conn.commit()
        messagebox.showinfo("Success", "Stock added successfully")
        qty_entry.delete(0, tk.END)

    def stock_out():
        if product_var.get() == "" or qty_entry.get() == "":
            messagebox.showerror("Error", "Please select product and enter quantity")
            return

        qty = int(qty_entry.get())
        pid = product_map[product_var.get()]

        cur.execute("SELECT quantity FROM products WHERE product_id = ?", (pid,))
        current_qty = cur.fetchone()[0]

        if qty > current_qty:
            messagebox.showerror("Error", "Not enough stock available")
            return

        cur.execute(
            "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
            (qty, pid)
        )

        cur.execute(
            "INSERT INTO stock_logs VALUES (NULL,?,?,?,?)",
            (pid, "OUT", qty, datetime.now())
        )

        conn.commit()
        messagebox.showinfo("Success", "Stock removed successfully")
        qty_entry.delete(0, tk.END)

    # ---------- BUTTONS ----------
    tk.Button(
        card, text="⬆ Stock IN",
        bg=t["success"], fg="white",
        font=("Segoe UI", 12, "bold"),
        bd=0, pady=10,
        command=stock_in
    ).pack(pady=15, padx=20, fill="x")

    tk.Button(
        card, text="⬇ Stock OUT",
        bg=t["danger"], fg="white",
        font=("Segoe UI", 12, "bold"),
        bd=0, pady=10,
        command=stock_out
    ).pack(padx=20, fill="x")
