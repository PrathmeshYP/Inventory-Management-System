import tkinter as tk
from database import connect_db
import theme

def product_window():
    conn = connect_db()
    cur = conn.cursor()
    t = theme.current_theme

    win = tk.Toplevel()
    win.geometry("480x550")
    win.title("Product Management")
    win.config(bg=t["bg"])

    tk.Label(win, text="Product Management",
             font=("Segoe UI", 16, "bold"),
             bg=t["bg"], fg=t["primary"]).pack(pady=20)

    card = tk.Frame(win, bg=t["card"])
    card.pack(padx=30, pady=10, fill="both", expand=True)

    fields = ["Product Name", "Category", "Price",
              "Quantity", "Supplier ID", "Min Stock"]
    entries = []

    for f in fields:
        tk.Label(card, text=f, bg=t["card"],
                 fg=t["text"], font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10, 0))
        e = tk.Entry(card, font=("Segoe UI", 11))
        e.pack(padx=20, fill="x")
        entries.append(e)

    def add_product():
        cur.execute("""
        INSERT INTO products VALUES (NULL,?,?,?,?,?,?)
        """, (
            entries[0].get(),
            entries[1].get(),
            float(entries[2].get()),
            int(entries[3].get()),
            int(entries[4].get()),
            int(entries[5].get())
        ))
        conn.commit()
        for e in entries:
            e.delete(0, tk.END)

    tk.Button(card, text="💾 Save Product",
              bg=t["primary"], fg="white",
              font=("Segoe UI", 12, "bold"),
              bd=0, pady=10,
              command=add_product).pack(pady=25, padx=20, fill="x")
