import connect
import datetime
import random

class MainMenu:
    def __init__(self, session):
        self.ssn = session.ssn
        self.phone = session.phone


    def send_money(self, cancel_reason=None):
        stid = random.randint(10000, 99999)
        recipient = input("Enter the phone number of the recipient: ")
        amount = float(input("How much money would you like to send? $"))
        date = datetime.datetime.now()
        memo = input("Add a memo: ")

        return connect.exec(f"""INSERT INTO SEND_TRANSACTION VALUES
            ({stid}, {amount}, TIMESTAMP '{date}', '{memo}',
            '{cancel_reason}', '{recipient}', '{self.ssn}');

            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+{amount} 
            WHERE PhoneNo='{recipient}';

            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-{amount}
            WHERE PhoneNo='{self.phone}';""")


    def request_money(self):
        rtid = random.randint(10000, 99999)
        sender = input("Enter the SSN of the sender: ")
        phone = input("Their phone number: ")
        amount = float(input("How much money would you like to request? $"))
        date = datetime.datetime.now()
        memo = input("Add a memo: ")
        percentage = 1
        return connect.exec(f"""INSERT INTO REQUEST_TRANSACTION VALUES
            ({rtid}, {amount}, TIMESTAMP '{date}', '{memo}', '{sender}');
            INSERT INTO RT_FROM VALUES ({rtid}, '{phone}', {percentage});""")
