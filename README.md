# 📦 Inventory Management System (Python)

A complete **Inventory Management System** developed using **Python, Tkinter, and SQLite** with a modern **Dark / Light Mode GUI**.  
This project allows users to manage products, suppliers, and stock efficiently with real-time database updates.

---

## 🚀 Key Features

- 📦 Product Management (Add, update, delete products)
- 🏭 Supplier Management
- 📊 Stock Management (Stock IN & Stock OUT)
- 📋 View Available Stock with quantity
- 🌙 Dark Mode / ☀ Light Mode toggle
- 🗄️ SQLite database (auto-created)
- 🖥️ Advanced GUI using Tkinter & ttk
- ✅ Input validation & error handling

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **GUI:** Tkinter, ttk
- **Database:** SQLite
- **Architecture:** Modular (separate files for each feature)

---

## 📂 Project Structure

Inventory_Management_System

├── main.py

├── database.py 

├── theme.py 

├── product.py 

├── supplier.py 

├── stock.py 

├── view_stock.py 

└── inventory.db 

##🧾 How Stock Management Works

- Products are stored in the products table
- Each product has a quantity column
- Stock IN → increases quantity
- Stock OUT → decreases quantity (no negative stock allowed)
- Available stock is displayed using a Treeview table
- All updates are saved permanently in SQLite

##📋 Available Stock Feature

Click “View Available Stock” button

Opens a new window

Displays:

Product ID

Product Name

Category

Quantity

Price

Data is fetched live from the database

🎨 Dark / Light Mode

Toggle theme from the main dashboard

Applies to all windows

Improves usability and modern appearance

Centralized theme control using theme.py

🧪 Future Enhancements

🔴 Low stock warning

🔍 Product search & filter

📤 Export stock report (CSV / PDF)

🔐 Login system with roles

📈 Graphs & analytics

📸 Screenshots (Optional)

Add screenshots of the dashboard, stock window, and dark/light mode here.

👨‍💻 Author

Prathmesh Yadav Patil
Python Developer | GUI & Database Applications

📄 License

This project is created for educational and learning purposes.
