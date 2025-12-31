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
- 🗄️ SQLite database
- 🖥️ Advanced GUI using Tkinter & ttk
- ✅ Input validation & error handling

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **GUI:** Tkinter, ttk
- **Database:** SQLite
- **Architecture:** Modular 

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

---

## 🧾 How Stock Management Works

- Products are stored in the products table
- Each product has a quantity column
- Stock IN → increases quantity
- Stock OUT → decreases quantity 
- Available stock is displayed using a Treeview table
- All updates are saved permanently in SQLite

---

## Screenshots

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/521aa3ca-ff4b-4462-983f-16b74df4222b" width="800"></td>
    <td><img src="https://github.com/user-attachments/assets/c212c399-019e-445c-b164-973e33769c29" width="800"></td>
    <td><img src="https://github.com/user-attachments/assets/1618d0bc-41fd-42fe-81a0-9c44485c41a5" width="800"></td>
    <td><img src="https://github.com/user-attachments/assets/5ea81a9f-492d-429a-86b6-d6aa381b17d9" width="800"></td>
  </tr>
</table>

## 🎨 Dark / Light Mode

- Toggle theme from the main dashboard
- Applies to all windows
- Improves usability and modern appearance
- Centralized theme control using theme.py

  ---
  
## 🧪 Future Enhancements

🔴 Low stock warning

🔍 Product search & filter

📤 Export stock report (CSV / PDF)

🔐 Login system with roles

📈 Graphs & analytics

---

## Screenshots 


## 👨‍💻 Author

Prathmesh Yadav Patil
Python Developer | GUI & Database Applications

---

## 📄 License

This project is created for educational and learning purposes.
