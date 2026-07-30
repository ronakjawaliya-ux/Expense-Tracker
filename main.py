import json
from datetime import datetime


def save_expenses(expenses):
    try:
        with open('expenses.json', 'w') as outfile:
            json.dump(expenses, outfile, indent=4)

    except Exception as e:
        print('Error saving expenses to file:', e)


def load_expenses():
    try:
        with open('expenses.json', 'r') as expenses_file:
            return json.load(expenses_file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


expenses = load_expenses()



while True:
    print('\n======== EXPENSE TRACKER ========\n')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Search Expense')
    print('4. Update Expense')
    print('5. Delete Expense')
    print('6. Total Expense')
    print('7. Expense Analysis')
    print('8. Exit')

    # Validating from ValueError
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid choice: it should be an integer')
        continue

    # Validating the Choice option
    if choice < 1 or choice > 8:
        print("Choice must be between 1 and 8")
        continue



    # 1. Add Expense
    if choice == 1:

        try:
            expense_id = int(input('Enter expense id: '))
        except ValueError:
            print('Invalid choice: it should be an integer')
            continue

        if expense_id <= 0:
            print('Invalid choice: Expense ID must be positive int')
            continue

        found = False
        for existing_expense in expenses:
            if existing_expense['id'] == expense_id:
                found = True
                print(f'Expense ID {expense_id} already exists')
                break

        if not found:

            while True:
                date = input('Enter expense date: ')

                try:
                    date = datetime.strptime(date, '%d-%m-%Y')
                    date = date.strftime('%d-%m-%Y')
                    break

                except ValueError:
                    print('Invalid date')



            categories = ['Food',
                          'Transport',
                          'Shopping',
                          'Bills',
                          'Entertainment',
                          'Health',
                          'Education',
                          'Other'
            ]

            for index, category in enumerate(categories, start=1):
                print(f'{index}. {category}')

            while True:

                try:
                    category_choice = int(input('Enter your choice: '))

                except ValueError:
                    print('Invalid choice: it should be an integer')
                    continue

                if category_choice < 1 or category_choice > 8:
                    print('Choice must be between 1 and 8')
                    continue

                category = categories[category_choice - 1]
                break

            while True:

                description = input('Enter expense description: ').strip()

                if not description:
                    print('Description cannot be empty')
                    continue

                break


            while True:

                try:
                    amount = float(input('Enter expense amount: '))
                except ValueError:
                    print('Invalid amount')
                    continue

                if amount <= 0:
                    print('Invalid amount')
                    continue

                break

            expense = {
                'id': expense_id,
                'date': date,
                'category': category,
                'amount': amount,
                'description': description,

            }

            expenses.append(expense)
            save_expenses(expenses)
            print(f'Expense ID {expense_id} added successfully!')


    # 2. View Expenses
    elif choice == 2:
        if not expenses:
            print('No expenses found!')
            continue

        print('======== VIEW EXPENSES ========\n')

        for expense in expenses:
            print('=================================\n')
            print(f'Expense ID {expense["id"]}')
            print(f'Date: {expense["date"]}')
            print(f'Category: {expense["category"]}')
            print(f'Description: {expense["description"]}')
            print(f'Amount: {expense["amount"]:.2f}')
            print('=================================\n')
























