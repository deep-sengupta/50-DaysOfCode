# Expense Tracker
This is a simple Expense Manager application built using Python. It uses `Tkinter` for the GUI, and `SQLite` as the backend database to store records of expenses. The application allows users to add, update, delete, and view expenses, as well as calculate the total balance and total amount spent.
<p align="center"><img width="853" alt="Screenshot 2024-09-20 at 02 30 16" src="https://github.com/user-attachments/assets/83291abe-9c94-44c3-96c7-f5a53974c256"></p>

## Features
- **Add Expense**: Add a new expense with an item name, price, and date of purchase.
- **View Expenses**: Fetch and display all records in a tabular form.
- **Update Record**: Modify an existing expense record.
- **Delete Record**: Remove an unwanted expense record.
- **Total Balance**: Calculate the total remaining balance.
- **Total Spent**: Calculate the total amount spent.

## Requirements
To use this script, you need the following dependencies installed:
- Python 3.x
- `SQLite`

## Database Schema
The application uses a simple SQLite database with the following schema:
- Table Name: `expense_record`
- Columns:
  - `item_name`: Name of the expense item (text)
  - `item_price`: Price of the item (float)
  - `purchase_date`: Date of purchase (date)