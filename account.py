import connect

class Account:
    def __init__(self, session):
        self.ssn = session.ssn
        self.phone = session.phone

    def account_info(self):
        print(connect.select_exec(f"""SELECT *
                                    FROM USER_ACCOUNT
                                    WHERE SSN='{self.ssn}';\n"""))

    def modify_name(self):
        name = input("Enter your new name: ")
        return connect.exec(f"""UPDATE USER_ACCOUNT
                                SET Name='{name}' 
                                WHERE SSN='{self.ssn}'""")

    def add_email_address(self):
        email = input("New email: ")
        verified = 1
        return connect.exec(f"""INSERT INTO ELEC_ADDRESS VALUES('{email}','{verified}', 'EMAIL');\n
                                INSERT INTO EMAIL VALUES('{email}','{self.ssn}');\n""")

    def remove_email_address(self, email):
        email = input("Email to remove: ")
        return connect.exec(f"DELETE FROM ELEC_ADDRESS WHERE Identifier='{email}';\n"
                            f"DELETE FROM EMAIL WHERE Identifier='{email}';\n"
                            f"UPDATE SEND_TRANSACTION"
                            f"SET Identifier=Null"
                            f"WHERE Identifier='{email}';\n"
                            f"UPDATE RT_FROM"
                            f"SET Identifier=Null"
                            f"WHERE Identifier='{email}';\n")

    def update_phone_number(self):
        phone = input("New Phone: ")

        return connect.exec(f"""UPDATE ELEC_ADDRESS
                                SET Identifier='{phone}'
                                WHERE Identifier=   (SELECT PhoneNo
                                                    FROM USER_ACCOUNT
                                                    WHERE SSN='{self.ssn}');
                                UPDATE SEND_TRANSACTION
                                SET Identifier='{phone}'
                                WHERE Identifier=   (SELECT PhoneNo
                                                    FROM USER_ACCOUNT
                                                    WHERE SSN='{self.ssn}');
                                UPDATE RT_FROM
                                SET Identifier='{phone}'
                                WHERE Identifier=   (SELECT PhoneNo
                                                    FROM USER_ACCOUNT
                                                    WHERE SSN='{self.ssn}');
                                UPDATE USER_ACCOUNT
                                SET PhoneNo='{phone}'
                                WHERE SSN='{self.ssn}';""")

    def add_bank_account(self):
        banumber = input("Add Bank Account Number: ")
        bankid = input("Bank ID: ")
        return connect.exec(f"""INSERT INTO BANK_ACCOUNT
                                VALUES ('{bankid}', '{banumber}')
                                WHERE Identifier=(SELECT BANumber
                                                  FROM USER_ACCOUNT
                                                  WHERE SSN='{self.ssn}');
                                UPDATE USER_ACCOUNT
                                SET BANumber='{banumber}'
                                WHERE SSN='{self.ssn}';""")
    def remove_bank_account(self):
        banumber = input("Add Bank Account: ")
        bankid = input("Bank ID: ")
        return connect.exec(f"""INSERT INTO BANK_ACCOUNT
                                VALUES ('{bankid}', '{banumber}')
                                WHERE Identifier=(SELECT BANumber
                                                  FROM USER_ACCOUNT
                                                  WHERE SSN='{self.ssn}');
                                UPDATE USER_ACCOUNT
                                SET BANumber='{banumber}'
                                WHERE SSN='{self.ssn}';""")
