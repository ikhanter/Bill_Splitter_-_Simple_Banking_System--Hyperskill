import random, sys, sqlite3


class Card:
    bin = '400000'

    def __init__(self):
        self.pin = ''
        self.acc_id = ''
        self.balance = 0
        cur.execute('SELECT id FROM card;')
        ids = cur.fetchall()
        for i in range(9):
            self.acc_id += str(random.randint(0, 9))
        while int(self.acc_id) in ids:
            self.acc_id = ''
            for i in range(9):
                self.acc_id += str(random.randint(0, 9))
        sum = 0
        pre_sum = Card.bin + self.acc_id
        i = 0
        while i <= 14:
            char = int(pre_sum[i])
            if i % 2 == 0:
                char *= 2
            if char > 9:
                char -= 9
            i += 1
            sum += char
        if sum % 10 == 0:
            checksum = '0'
        else:
            checksum = str(10 - sum % 10)
        self.number = pre_sum + checksum
        for i in range(4):
            self.pin += str(random.randint(0, 9))
        cur.execute(f'INSERT INTO card (id, number, pin, balance)  \
                    VALUES ({self.acc_id}, {self.number}, {self.pin}, {self.balance})')
        conn.commit()

n = 1

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER);')
except:
    pass
conn.commit()

while n != 0:
    z = 0
    l = 1
    print('''1. Create an account
2. Log into account
0. Exit''')
    print()
    n = int(input())
    if n == 1:
        print('Your card has been created')
        print('Your card number:')
        testcard = Card()
        print(testcard.number)
        print('Your card PIN:')
        print(testcard.pin)
        print()
    elif n == 2:
        print('Enter your card number:')
        check_number = input()
        print('Enter your PIN:')
        check_pin = input()
        print()
        cur.execute(f'SELECT number, pin FROM card WHERE number = {check_number} AND pin = {check_pin};')
        check_sum = cur.fetchone()
        if check_sum:
            print('You have successfully logged in!')
            print()
            while l != 5:
                print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
                l = int(input())
                print()
                if l == 1:
                    cur.execute(f'SELECT balance FROM card WHERE number = {check_number};')
                    blnc = cur.fetchone()
                    print('Balance:', blnc)
                    print()
                elif l == 0:
                    sys.exit()
                elif l == 2:
                    print('Enter the amount of money to deposit:')
                    money = int(input())
                    cur.execute(f'SELECT balance FROM card WHERE number = {check_number};')
                    money += cur.fetchone()[0]
                    cur.execute(f'UPDATE card SET balance={money} WHERE number = {check_number};')
                    conn.commit()
                    print()
                    print('Income was added!')
                    print()
                elif l == 3:
                    key_error = 0
                    sum = 0
                    z = 0
                    print('Transfer')
                    print('Enter card number:')
                    transfer_card = input()
                    cur.execute(f'SELECT number FROM card WHERE number = {transfer_card};')
                    check_exist_transcard = cur.fetchone()
                    print()
                    if not check_exist_transcard:
                        print('Such a card does not exist.')
                        print()
                        key_error = 1
                    while z <= 14:
                        char = int(transfer_card[z])
                        if z % 2 == 0:
                            char *= 2
                        if char > 9:
                            char -= 9
                        z += 1
                        sum += char
                    sum += int(transfer_card[-1])
                    if sum % 10 != 0:
                        key_error = 1
                        print('Probably you made a mistake in the card number. Please try again!')
                        print()
                    if key_error == 0:
                        print('Enter how much money you want to transfer:')
                        money = int(input())
                        cur.execute(f'SELECT balance FROM card WHERE number = {check_number};')
                        blnc = cur.fetchone()[0]
                        if money > blnc:
                            print('Not enough money!')
                            print()
                        else:
                            blnc -= money
                            cur.execute(f'UPDATE card SET balance = {blnc} WHERE number = {check_number};')
                            cur.execute(f'SELECT balance FROM card WHERE number = {transfer_card};')
                            money += cur.fetchone()[0]
                            cur.execute(f'UPDATE card SET balance = {money} WHERE number = {transfer_card};')
                            conn.commit()
                            print('Success!')
                            print()
                elif l == 4:
                    cur.execute(f'DELETE FROM card WHERE number = {check_number}')
                    conn.commit()
                    l = 5
                    print()
                    print('The account has been closed!')
                    print()

            print('You have successfully logged out!')
        else:
            print('Wrong card number or PIN!')
            print()
conn.commit()
print('Bye!')
