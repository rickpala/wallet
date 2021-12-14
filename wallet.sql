CREATE TABLE IF NOT EXISTS BANK_ACCOUNT(BankID  VARCHAR(10) NOT NULL, 
                                        BANumber VARCHAR(10) NOT NULL, 
                                        CONSTRAINT BA_PK PRIMARY KEY (BankID, BANumber) );


CREATE TABLE IF NOT EXISTS ELEC_ADDRESS(Identifier  VARCHAR(30) NOT NULL, 
                                        Verified BIT, 
                                        Type CHAR(5), 
                                        CONSTRAINT EA_PK PRIMARY KEY (Identifier) );
CREATE TABLE IF NOT EXISTS USER_ACCOUNT(SSN  CHAR(9) NOT NULL, 
                                        Name VARCHAR(40), 
                                        PhoneNo VARCHAR(10), 
                                        Balance DECIMAL(10, 2), 
                                        BankID  VARCHAR(10), 
                                        BANumber VARCHAR(10), 
                                        PBAVerified  BIT, 
                                        CONSTRAINT UA_PK PRIMARY KEY (SSN), 
                                        CONSTRAINT UA_BA_FK FOREIGN KEY (BankID, BANumber) 
                                        REFERENCES BANK_ACCOUNT(BankID, BANumber) ON DELETE CASCADE ON UPDATE CASCADE, 
                                        CONSTRAINT UA_EA_FK FOREIGN KEY (PhoneNo) REFERENCES ELEC_ADDRESS(Identifier) ON DELETE CASCADE ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS HAS_ADDITIONAL(SSN  CHAR(9) NOT NULL, 
                                        BankID  VARCHAR(10) NOT NULL, 
                                        BANumber VARCHAR(10) NOT NULL, 
                                        Verified BIT, 
                                        CONSTRAINT HA_PK PRIMARY KEY (SSN, BankID, BANumber), 
                                        CONSTRAINT HA_BA_FK FOREIGN KEY (BankID, BANumber) 
                                        REFERENCES BANK_ACCOUNT(BankID, BANumber) ON DELETE CASCADE ON UPDATE CASCADE, 
                                        CONSTRAINT HA_UA_FK FOREIGN KEY (SSN) REFERENCES USER_ACCOUNT(SSN) ON DELETE CASCADE ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS SEND_TRANSACTION (STid  CHAR(5) NOT NULL, 
                                        Amount DECIMAL(10, 2), 
                                        Date_Time TIMESTAMP, 
                                        Memo VARCHAR(100), 
                                        Cancel_Reason VARCHAR(100), 
                                        Identifier VARCHAR(30), 
                                        SSN CHAR(9), 
                                        CONSTRAINT ST_PK PRIMARY KEY (STid), 
                                        CONSTRAINT ST_UA_FK FOREIGN KEY (SSN) REFERENCES USER_ACCOUNT(SSN) ON DELETE CASCADE ON UPDATE CASCADE, 
                                        CONSTRAINT ST_EA_FK FOREIGN KEY (Identifier) REFERENCES ELEC_ADDRESS(Identifier) ON DELETE CASCADE ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS EMAIL(EmailAdd VARCHAR(30) NOT NULL, 
                                        SSN CHAR(9), 
                                        CONSTRAINT EMAIL_PK PRIMARY KEY (EmailAdd), 
                                        CONSTRAINT EMAIL_UA_FK FOREIGN KEY (SSN) REFERENCES USER_ACCOUNT(SSN) ON DELETE CASCADE ON UPDATE CASCADE, 
                                        CONSTRAINT EMAIL_EA_FK FOREIGN KEY (EmailAdd) REFERENCES ELEC_ADDRESS(Identifier) ON DELETE CASCADE ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS REQUEST_TRANSACTION(RTid CHAR(5) NOT NULL, 
                                        Amount DECIMAL(10, 2), 
                                        Date_Time TIMESTAMP, 
                                        Memo  VARCHAR(100), 
                                        SSN CHAR(9), 
                                        CONSTRAINT RT_PK PRIMARY KEY (RTid), 
                                        CONSTRAINT RT_UA_FK FOREIGN KEY (SSN) REFERENCES USER_ACCOUNT(SSN) ON DELETE CASCADE ON UPDATE CASCADE );

CREATE TABLE IF NOT EXISTS RT_FROM(RTid CHAR(5) NOT NULL, 
                                        Identifier VARCHAR(30), 
                                        Percentage DECIMAL(10, 2), 
                                        CONSTRAINT FROM_PK PRIMARY KEY (RTid, Identifier), 
                                        CONSTRAINT FROM_RT_FK FOREIGN KEY (RTid) REFERENCES REQUEST_TRANSACTION(RTid) ON DELETE CASCADE ON UPDATE CASCADE, 
                                        CONSTRAINT FROM_EA_FK FOREIGN KEY (Identifier) REFERENCES ELEC_ADDRESS(Identifier) ON DELETE CASCADE ON UPDATE CASCADE );
