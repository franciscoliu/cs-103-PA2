'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''

# from transactions import Transaction
from category import Category
from transaction import Transaction

# transactions = Transaction('tracker.db')
category = Category('tracker.db')
transaction = Transaction('transaction.db')

# here is the menu for the tracker app

ME_NU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. clear the transaction database
'''


# pylint:disable=too-many-branches
# pylint:disable=too-many-statements
# pylint:disable=inconsistent-return-statements
# pylint:disable=no-else-return
# pylint:disable=consider-using-f-string
def process_choice(choice):
    '''user can choose each number to process choice
    frank wrote choice 4, 5, 6'''

    if choice == '0':
        return
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)

        # Added code
    elif choice == '4':
        cats = transaction.select_all()
        print_transactions(cats)
    elif choice == '5':
        item = input("item number: ")
        amount = int(input("item amount: "))
        categ = input("category name: ")
        date = int(input("transaction date: "))
        des = input("transaction description: ")
        cat = {'item_number': item, 'amount': amount,
               'category': categ, 'date': date, 'description': des}
        transaction.add(cat)
    elif choice == '6':
        delete_id = int(input("the rowid of the deleted transaction: "))
        transaction.delete(delete_id)
    elif choice == '7':
        # summarize_by_date.clear()
        dates = transaction.summarize_by_date()
        # summarize_by_date.extend(dates)
        print("Summarize by date")
        print_summarize_by_date(dates)
    elif choice == '8':
        dates = transaction.summarize_by_month()
        print("Summarize by month")
        print_summarize_by_month(dates)
    elif choice == '9':
        dates = transaction.summarize_by_year()
        print("Summarize by year")
        print_summarize_by_year(dates)
    elif choice == '10':
        # summarize_by_category.clear()
        summarize_category = transaction.summarize_by_category()
        # summarize_by_category.extend(summarize_category)
        print("Summarize by category")
        print_summarize_by_category(summarize_category)
    elif choice == '11':
        print(ME_NU)
    elif choice == '12':
        transaction.clear_database()
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return choice


# pylint:disable=bad-option-value
def print_summarize_by_category(items):
    '''summarize the datatable by category'''

    if len(items) == 0:
        print('no items to print for summarize by category')
        return
    print()
    print("%-10s %-10s" % ('category', 'total amount'))
    print('-' * 30)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10d" % values)


# pylint:disable=bad-option-value
def print_summarize_by_date(items):
    '''summarize the datatable by date'''

    if len(items) == 0:
        print('no items to print for summarize by date')
        return
    print()
    print("%-10s %-10s" % ('date', 'total amount'))
    print('-' * 30)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10d" % values)


# pylint:disable=bad-option-value
def print_summarize_by_month(items):
    '''summarize the datatable by month'''

    if len(items) == 0:
        print('no items to print for summarize by month')
        return
    print()
    print("%-10s %-10s" % ('month', 'total amount'))
    print('-' * 30)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10d" % values)


# pylint:disable=bad-option-value
def print_summarize_by_year(items):
    '''summarize the datatable by year'''

    if len(items) == 0:
        print('no items to print for summarize by year')
        return
    print()
    print("%-10s %-10s" % ('year', 'total amount'))
    print('-' * 30)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10d" % values)


def toplevel():
    ''' handle the user's choice, read the command args and process them '''

    print(ME_NU)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions
#
# pylint:disable=bad-option-value
def print_transactions(items):
    ''' print the transactions '''

    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-10s %-30s" % (
        'row_id', 'item_number', 'amount', 'category', 'date', 'description'))
    print('-' * 70)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s %-10d %-10s %-10d %-30s" % values)


# pylint:disable=bad-option-value
def print_category(cat):
    '''print detailed category'''

    print("%-3d %-10s %-30s" % (cat['rowid'], cat['name'], cat['desc']))


# pylint:disable=bad-option-value
def print_categories(cats):
    '''print categories'''

    print("%-3s %-10s %-30s" % ("id", "name", "description"))
    print('-' * 30)
    for cat in cats:
        print_category(cat)


# here is the main call!
if __name__ == "__main__":
    toplevel()
