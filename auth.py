import connect
USER_PK = 0 #Used for table joins and transaction selection per user 
class Auth:
    def __init__(self):
        pass

    def user_login(self, ssn, phone):
        global USER_PK
        USER_PK = ssn
        #TODO replaced with sql query to check for user in db
        print(f'User {ssn} with {phone} has signed in')

    def user_register(self, name, user_ssn, phone, email,verified=1):
        return connect.exec(f"""INSERT INTO ELEC_ADDRESS VALUES('{phone}','{verified}', 'PHONE');\n
                                INSERT INTO EMAIL VALUES('{email}','{user_ssn}');\n
                                INSERT INTO ELEC_ADDRESS VALUES('{email}','{verified}', 'EMAIL');\n
                                INSERT INTO USER_ACCOUNT(SSN, Name, PhoneNo) VALUES('{user_ssn}', '{name}', '{phone}');""")

