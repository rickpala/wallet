import connect
import datetime
import random

class Statements:
    def __init__(self, session):
        self.ssn = session.ssn
        self.phone = session.phone

    def statement_users_by_date_range(self, choice):
        user_name = input("Enter user's full name: ")
        start = input("Enter start date in MM-DD-YYYY: ")
        end = input("Enter end date in MM-DD-YYYY: ")
        
        if choice == "S":
            return connect.select_exec(f"""SELECT USER_ACCOUNT.Name, SUM(AMOUNT) AS Total 
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, SEND_TRANSACTION 
                                    WHERE USER_ACCOUNT.SSN=SEND_TRANSACTION.SSN 
                                        AND USER_ACCOUNT.Name='{user_name}' 
                                        AND SEND_TRANSACTION.Date_Time BETWEEN '{start}' AND '{end}'\n""")
        elif choice == "R":
            return connect.select_exec(f"""SELECT USER_ACCOUNT.NAME, SUM(Amount) AS Total
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, REQUEST_TRANSACTION NATURAL JOIN RT_FROM
                                    WHERE USER_ACCOUNT.Name='{user_name}'
                                    AND REQUEST_TRANSACTION.Date_Time BETWEEN '{start}' AND '{end}';\n""")


    def get_statement_by_month(self, ttype):
        month = input("Enter the month (MM): ")
        if ttype == 'S':
            return connect.select_exec(f"""SELECT STid, Date_Time
                                        FROM SEND_TRANSACTION
                                        WHERE SSN='{self.ssn}'
                                        GROUP BY STid, Date_Time;\n""")
        if ttype == 'R':
            return connect.select_exec(f"""SELECT RTid, Date_Time
                                        FROM REQUEST_TRANSACTION
                                        WHERE SSN='{self.ssn}'
                                        GROUP BY RTid, Date_Time;\n""")


    def get_largest_transactions(self, ttype):
        month = input("Enter the month (MM): ")
        if ttype == 'S':
            return connect.select_exec(f"""SELECT STid, Date_Time, MAX(Amount) AS Amount
                                        FROM SEND_TRANSACTION
                                        WHERE SSN='{self.ssn}'
                                        GROUP BY STid, Date_Time
                                        ORDER BY Amount;\n""")
        if ttype == 'R':
            return connect.select_exec(f"""SELECT RTid, Date_Time, MAX(Amount) AS Amount
                                        FROM REQUEST_TRANSACTION
                                        WHERE SSN='{self.ssn}'
                                        GROUP BY RTid, Date_Time
                                        ORDER BY Amount;\n""")


    def get_best_friends(self, ttype):
        raise NotImplementedError

    def statement_search(self):
        raise NotImplementedError