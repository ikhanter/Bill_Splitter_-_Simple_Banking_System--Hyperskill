import sys, random
participants = dict()
n = int(input('How much persons will eat now? '))
if n > 0:
    for i in input('Type the names of participants of the dinner: ').split():
        participants[i] = 0
    if len(participants) != n:
        participants = dict()
        print('The number of participants and amout of the names are not equal. Try again.')
        sys.exit()
else:
    print('Some errors occur. Maybe, you type the wrong number of dinner \
participants')
    sys.exit()

bill = int(input('Enter the total bill value: '))
print()
print('Do you want to use "Who is Lucky?" Write Yes/No')
option = input()
print()
if option == 'Yes':
    option = random.choice(list(participants.keys()))
    print(f'{option} is the Lucky One!')
    print()
elif option == 'No':
    print('No one is going to be lucky.')
    print()
if option != 'No':
    n -= 1
else:
    option = 0
if bill % n != 0:
    bill = round(bill / n, 2)
else:
    bill = bill // n
for man in participants:
    if man == option:
        participants[man] = 0
    else:
        participants[man] = bill
print(participants)
