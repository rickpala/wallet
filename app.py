import sys
import connect
import queries
from statements import Statements
from mainmenu import MainMenu
from auth import Auth
from account import Account
from search import Search

class Session:
    def __init__(self, ssn, phone):
        self.ssn = ssn
        self.phone = phone
    
    def end(self):
        self.ssn = None
        self.phone = None

def get_menu_selection(d):
    for k, v in d.items():
        print(f"[{v}] {k}")
    choice = int(input("Selection: "))
    print()  # newline
    return choice

main_menu = {"account": 1,
             "send_money": 2,
             "request_money": 3,
             "statements": 4,
             "search_transactions": 5,
             "sign_out": 0}

account_menu = {"account_info": 1,
                "modify_name": 2,
                "add_email_address": 3,
                "remove_email_address": 4,
                "update_phone_number": 5,
                "add_bank_account": 6,
                "remove_bank_account": 7,
                "main_menu": 0}

statement_menu = {"get_statement_by_dates": 1,
                  "get_statement_by_month": 2,
                  "get_largest_transactions": 3,
                  "get_best_friends": 4,
                  "main_menu": 0}

search_menu = {"user_email": 1,
               "user_phone": 2,
               "transaction_type": 3,
               "main_menu": 0}

authenticate_dict = {"login": 1,
                     "register": 2}

def handle_transaction(session, ttype):
    menu = MainMenu(session)
    if ttype == "send":
        print(menu.send_money())
    elif ttype == "request":
        print(menu.request_money())


def handle_search(session):
    while True:
        print("[SEARCH]")
        choice = get_menu_selection(search_menu)
        if choice == search_menu["user_email"]:
            raise NotImplementedError
        elif choice == search_menu["user_phone"]:
            raise NotImplementedError
        elif choice == search_menu["transaction_type"]:
            raise NotImplementedError
        elif choice == search_menu["main_menu"]:
            return

def handle_statements(session):
    stmts = Statements(session)
    while True:
        print("[STATEMENTS]")
        choice = get_menu_selection(statement_menu)

        print("[R] View Received Transactions")
        print("[S] View Sent Transactions")
        ttype = input("Selection: ")
        if choice == statement_menu["get_statement_by_dates"]:
            print(stmts.statement_users_by_date_range(ttype))
        elif choice == statement_menu["get_statement_by_month"]:
            print(stmts.get_statement_by_month(ttype))
        elif choice == statement_menu["get_largest_transactions"]:
            print(stmts.get_largest_transactions(ttype))
        elif choice == statement_menu["get_best_friends"]:
            print(stmts.get_best_friends(ttype))
        elif choice == statement_menu["main_menu"]:
            return

def handle_account(session):
    acct = Account(session)
    while True:
        print("[ACCOUNT MENU]")
        choice = get_menu_selection(account_menu)
        if choice == account_menu["account_info"]:
            print(acct.account_info())
        elif choice == account_menu["modify_name"]:
            print(acct.modify_name())
        elif choice == account_menu["add_email_address"]:
            print(acct.add_email_address())
        elif choice == account_menu["remove_email_address"]:
            print(acct.remove_email_address())
        elif choice == account_menu["update_phone_number"]:
            print(acct.update_phone_number())
        elif choice == account_menu["add_bank_account"]:
            print(acct.add_bank_account())
        elif choice == account_menu["remove_bank_account"]:
            print(acct.remove_bank_account())
        elif choice == account_menu["main_menu"]:
            return


def handle_login():
    user_ssn = input("Enter your SSN: ")
    user_phone = input("Enter your phone number: ")
    auth = Auth()
    print(auth.user_login(user_ssn, user_phone))

    session = Session(user_ssn, user_phone)
    while True:
        print("[MAIN MENU]")
        mm_choice = get_menu_selection(main_menu)

        if mm_choice == main_menu["account"]:
            print(handle_account(session))
        elif mm_choice == main_menu["send_money"]:
            print(handle_transaction(session, "send"))
        elif mm_choice == main_menu["request_money"]:
            print(handle_transaction(session, "request"))
        elif mm_choice == main_menu["statements"]:
            print(handle_statements(session))
        elif mm_choice == main_menu["search_transactions"]:
            print(handle_search(session))
        elif mm_choice == main_menu["sign_out"]:
            return # go back to home


def handle_registration():
    user_name = input("Enter your first and last name: ")
    user_ssn = int(input("Enter your SSN: "))
    user_phone = int(input("Enter your phone number: "))
    user_email = input("Enter your email address: ")
    auth = Auth()
    print(auth.user_register(user_name, user_ssn, user_phone, user_email))

    session = Session(user_ssn, user_phone)


if __name__ == "__main__":
    print("Welcome to WALLET!")
    print("Would you like to login or register?")

    while True:
        auth = input("Type 'login' or 'register': ")
        if auth == "login":
            handle_login()
        elif auth == "register":
            handle_registration()
        else:
            print("Unknown input. Exiting...")
            sys.exit()