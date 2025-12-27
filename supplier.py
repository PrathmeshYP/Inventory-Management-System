import tkinter as tk
from database import connect_db
import theme

def supplier_window():
    conn = connect_db()
    cur = conn.cursor()
    t = theme.current_theme

    win = tk.Toplevel()
    win.geometry("450x420")
    win.title("Supplier Management")
    win.config(bg=t["bg"])

    tk.Label(win, text="Supplier Management",
             font=("Segoe UI", 16, "bold"),
             bg=t["bg"], fg=t["primary"]).pack(pady=20)

    card = tk.Frame(win, bg=t["card"])
    card.pack(padx=30, pady=10, fill="both", expand=True)

    def field(label):
        tk.Label(card, text=label, bg=t["card"],
                 fg=t["text"], font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10, 0))
        e = tk.Entry(card, font=("Segoe UI", 11))
        e.pack(padx=20, fill="x")
        return e

    name = field("Supplier Name")
    phone = field("Phone")
    email = field("Email")

    def add_supplier():
        cur.execute("INSERT INTO suppliers VALUES (NULL,?,?,?)",
                    (name.get(), phone.get(), email.get()))
        conn.commit()
        name.delete(0, tk.END)
        phone.delete(0, tk.END)
        email.delete(0, tk.END)

    tk.Button(card, text="➕ Add Supplier",
              bg=t["success"], fg="white",
              font=("Segoe UI", 12, "bold"),
              bd=0, pady=10,
              command=add_supplier).pack(pady=25, padx=20, fill="x")
