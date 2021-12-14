from faker import Faker
import random
import decimal

entries = 10
domain = range(1000000000, 9999999999)
BIDs = random.sample(domain, entries)
BANs = random.sample(domain, entries)
SSNs = random.sample(domain, entries)
PNs = random.sample(domain, entries)

fake = Faker()
fake.seed_instance(4321)
commands = []
for SSN, BID, BAN, PN in zip(SSNs, BIDs, BANs, PNs):
    name = fake.name()
    verified = 1
    balance = float(decimal.Decimal(random.randrange(0, 1000000))/100)
    
    commands.append(f"INSERT INTO BANK_ACCOUNT VALUES('{BID}', '{BAN}');\n")
    commands.append(f"INSERT INTO ELEC_ADDRESS VALUES('{PN}','{verified}');\n")
    commands.append(f"INSERT INTO USER_ACCOUNT VALUES('{SSN}', '{name}', '{PN}', {balance}, '{BID}', '{BAN}', '{verified}');\n")
    
with open("fake_data.sql", "w") as sql_file:
    sql_file.writelines(commands)