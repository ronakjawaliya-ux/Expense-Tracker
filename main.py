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



    # 1. ADD EXPENSE
    if choice == 1:

        # Validate ID
        try:
            expense_id = int(input('Enter expense id: '))
        except ValueError:
            print('Invalid choice: it should be an integer')
            continue

        # Prevent Negative and Zero Age
        if expense_id <= 0:
            print('Invalid choice: Expense ID must be positive int')
            continue

        found = False
        # Prevent Duplication
        for existing_expense in expenses:
            if existing_expense['id'] == expense_id:
                found = True
                print(f'Expense ID {expense_id} already exists')
                break

        if not found:

            while True:
                # Validate Date
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
                # Validate Category
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
                # Validate Description
                description = input('Enter expense description: ').strip()

                if not description:
                    print('Description cannot be empty')
                    continue

                break


            while True:
                # Validate Amount
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


    # 2. VIEW EXPENSES
    elif choice == 2:

        if not expenses:
            print('No expenses found!')
            continue

        print('======== VIEW EXPENSES ========\n')

        for expense in expenses:
            print('=================================\n')
            print(f'Expense ID     : {expense["id"]}')
            print(f'Date           : {expense["date"]}')
            print(f'Category       : {expense["category"]}')
            print(f'Description    : {expense["description"]}')
            print(f'Amount         : ₹{expense["amount"]:.2f}')
            print('=================================\n')


    # 3. SEARCH EXPENSE
    elif choice == 3:

        if not expenses:
            print('No expenses found!')
            continue

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
                print('\nExpense Details\n')
                print('=================================\n')
                print(f'Expense ID     : {existing_expense["id"]}')
                print(f'Date           : {existing_expense["date"]}')
                print(f'Category       : {existing_expense["category"]}')
                print(f'Description    : {existing_expense["description"]}')
                print(f'Amount         : ₹{existing_expense["amount"]:.2f}')
                print('=================================\n')
                found = True
                break

        if not found:
            print('\nExpense not found\n')

    # 4. UPDATE EXPENSE
    elif choice == 4:

        if not expenses:
            print('No expenses found!')
            continue

        # Validate ID
        try:
            expense_id = int(input('Enter expense id: '))
        except ValueError:
            print('Invalid choice: it should be an integer')
            continue

        if expense_id <= 0:
            print('Invalid choice: Expense ID must be positive int')
            continue

        found = False
        updated = False

        for existing_expense in expenses:
            if existing_expense['id'] == expense_id:
                found = True
                print('=================================\n')
                print(f'Expense ID     : {existing_expense["id"]}')
                print(f'Date           : {existing_expense["date"]}')
                print(f'Category       : {existing_expense["category"]}')
                print(f'Description    : {existing_expense["description"]}')
                print(f'Amount         : ₹{existing_expense["amount"]:.2f}')
                print('=================================\n')

                while True:

                    print('1. Date')
                    print('2. Category')
                    print('3. Description')
                    print('4. Amount')
                    print('5. Cancel')

                    # Validating from ValueError
                    try:
                        update_choice = int(input('Enter your update choice: '))
                    except ValueError:
                        print('Invalid update choice: it should be an integer')
                        continue

                    # Validating the update choice option
                    if update_choice < 1 or update_choice > 5:
                        print("Update choice must be between 1 and 5")
                        continue

                    if update_choice == 1:

                        while True:
                            # Validate Date
                            new_date = input('Enter expense new date: ')

                            try:
                                date = datetime.strptime(new_date, '%d-%m-%Y')
                                date = date.strftime('%d-%m-%Y')
                                existing_expense['date'] = date
                                updated = True
                                break

                            except ValueError:
                                print('Invalid date')

                    if update_choice == 2:

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
                            # Validate Category
                            try:
                                update_category_choice = int(input('Enter your update category choice: '))

                            except ValueError:
                                print('Invalid choice: it should be an integer')
                                continue

                            if update_category_choice < 1 or update_category_choice > 8:
                                print('Update choice must be between 1 and 8')
                                continue

                            category = categories[update_category_choice - 1]
                            existing_expense['category'] = category
                            updated = True
                            break



                    if update_choice == 3:

                        while True:
                            # Validate Description
                            update_description = input('Enter expense description: ').strip()

                            if not update_description:
                                print('Update description cannot be empty')
                                continue
                            existing_expense['description'] = update_description
                            updated = True
                            break



                    if update_choice == 4:

                        while True:
                            # Validate Amount
                            try:
                                update_amount = float(input('Enter expense update amount: '))
                            except ValueError:
                                print('Invalid amount')
                                continue

                            if update_amount <= 0:
                                print('Invalid amount')
                                continue
                            existing_expense['amount'] = update_amount
                            updated = True
                            break


                    if update_choice == 5:
                        print('Update cancelled')
                        break

                    if updated:
                        break

                break

        if not found:
            print('Expense not found')

        if updated:
            save_expenses(expenses)
            print(f'Expense ID {expense_id} updated successfully!')


    # 5. DELETE EXPENSE
    elif choice == 5:

        if not expenses:
            print('No expenses found!')
            continue

        try:
            delete_expense_id = int(input('Enter Expense ID to delete: '))
        except ValueError:
            print('Expense ID should be an integer')
            continue

        if delete_expense_id <= 0:
            print('Invalid choice: Expense ID must be positive int')
            continue


        found = False

        for existing_expense in expenses:
            if existing_expense['id'] == delete_expense_id:
                found = True
                print('=================================\n')
                print(f'Expense ID     : {existing_expense["id"]}')
                print(f'Date           : {existing_expense["date"]}')
                print(f'Category       : {existing_expense["category"]}')
                print(f'Description    : {existing_expense["description"]}')
                print(f'Amount         : ₹{existing_expense["amount"]:.2f}')
                print('=================================\n')

                while True:
                    confirm = input("Are you sure you want to delete this expense? (Y/N): ").strip().upper()

                    if confirm == 'Y':
                        print("Deleting expense...")
                        expenses.remove(existing_expense)
                        print(f'Expense ID {delete_expense_id} deleted successfully!')
                        save_expenses(expenses)
                        break

                    elif confirm == 'N':
                        print("Canceling deletion...")
                        break

                    else:
                        print('Please enter Y or N')

                break

        if not found:
            print('Expense not found.')

    # 6. TOTAL EXPENSE
    elif choice == 6:

        if not expenses:
            print('No expenses found!')
            continue

        total = 0
        for existing_expense in expenses:
            total += existing_expense['amount']

        print(f'Total Expense: ₹{total:.2f}')

    # 7. EXPENSE ANALYSIS
    elif choice == 7:

        # Validating Empty Expense
        if not expenses:
            print('No expenses found!')
            continue

        # Total Expense
        expense_count = len(expenses)
        total = 0
        for existing_expense in expenses:
            total += existing_expense['amount']

        # Average Expense
        average = total / expense_count

        # Highest Expense
        highest_expense = max(expenses, key=lambda x: x['amount'])

        # Lowest Expense
        lowest_expense = min(expenses, key=lambda x: x['amount'])



        category_totals = {}

        for existing_expense in expenses:
            category = existing_expense['category']
            category_totals[category] = category_totals.get(category, 0) + existing_expense['amount']

        print('======== EXPENSE ANALYSIS ========\n')
        print(f'Total Expense       : ₹{total:.2f}')
        print(f'Average Expense     : ₹{average:.2f}')
        print(f'Highest Expense     : ₹{highest_expense["amount"]:.2f}')
        print(f'Lowest Expense      : ₹{lowest_expense["amount"]:.2f}')
        print('==================================\n')

        print('======== CATEGORY-WISE SPENDING ========\n')
        for category, amount in category_totals.items():
            print(f'{category:<18}: ₹{amount:.2f}')
        print('========================================\n')


    #8. EXIT
    elif choice == 8:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")
        print("Please enter a number between 1 and 8.")


















































