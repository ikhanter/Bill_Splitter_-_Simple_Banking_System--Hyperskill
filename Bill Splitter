import random

participants = dict()
print('How much persons will eat now? ')
n = int(input())
print()
if n > 0:
    print('Type the names of participants: ')
    for i in range(n):
        participants[input()] = 0
    print()
    print('Enter the total bill value:')
    bill = int(input())
    for i in participants:
        participants[i] = bill
    print()
    print('Do you want to use "Who is Lucky?" Write Yes/No')
    option = input()
    print()
    if option == 'Yes':
        option = random.choice(list(participants.keys()))
        print(f'{option} is the Lucky One!')
        print()
        bill = round(bill / (n - 1), 2)
        for i in participants:
            if i == option:
                participants[i] = 0
            else:
                participants[i] = bill
        print(participants)
    else:
        print('No one is going to be lucky')
        print()
        bill = round(bill / n , 2)
        for i in participants:
            participants[i] = bill
        print(participants)
else:
    print("No one is joining for the party")
