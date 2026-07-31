# 📚 Expense Tracker - Features

This project is a **menu-driven Expense Tracker** developed using **Python**. It allows users to manage their daily expenses efficiently while storing data permanently in a JSON file.

---

# 💰 Expense Management Features

## ➕ Add Expense

* Add a new expense to the tracker.
* Stores:

  * Expense ID
  * Date
  * Category
  * Description
  * Amount
* Prevents duplicate Expense IDs.
* Validates date format (`DD-MM-YYYY`).
* Validates category selection.
* Prevents empty descriptions.
* Validates positive expense amount.
* Saves data permanently to the JSON file.

---

## 📋 View Expenses

* Displays all saved expenses.
* Shows:

  * Expense ID
  * Date
  * Category
  * Description
  * Amount

---

## 🔍 Search Expense

* Search an expense using its Expense ID.
* Displays complete expense details.
* Shows an appropriate message if the expense is not found.

---

## ✏️ Update Expense

* Update an existing expense by Expense ID.
* Allows updating:

  * Date
  * Category
  * Description
  * Amount
* Includes an option to cancel the update.
* Saves updated information permanently.

---

## 🗑 Delete Expense

* Delete an expense using its Expense ID.
* Displays expense details before deletion.
* Asks for confirmation (`Y/N`) before deleting.
* Removes the expense permanently from the JSON file.

---

## 💵 Total Expense

* Calculates the total amount of all recorded expenses.
* Displays the total expense in Indian Rupees (₹).

---

## 📊 Expense Analysis

Provides a summary of recorded expenses, including:

* Total Expense
* Average Expense
* Highest Expense
* Lowest Expense
* Category-wise Spending

---

# 💾 Data Storage

* Stores all expense records in **expenses.json**.
* Automatically loads saved expenses when the program starts.
* Automatically saves changes after adding, updating, or deleting expenses.

---

# ✅ Input Validation

The project includes validation for:

* Expense ID must be a positive integer.
* Duplicate Expense ID prevention.
* Date format validation (`DD-MM-YYYY`).
* Category selection validation.
* Description cannot be empty.
* Amount must be greater than zero.
* Integer validation.
* Float validation.
* File not found handling.
* JSON decoding error handling.

---

# 🚪 Exit

* Safely exits the Expense Tracker application.
