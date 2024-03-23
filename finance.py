import generation as g
import edit as e
import random
import json

def withdraw(team, amount, type):
    data = g.read_Json('financials.json')

    default_budget = 0

    if type.lower() == 't':
        for i in range(len(data['teams'])):
            if data['teams'][i]['name'].lower() == team.lower():
                default_budget = data['teams'][i]['transfer']
                break

        data['teams'][i]['transfer'] = default_budget - amount

    if type.lower() == 'f':
        for i in range(len(data['teams'])):
            if data['teams'][i]['name'].lower() == team.lower():
                default_budget = data['teams'][i]['facilities']
                break

        data['teams'][i]['facilities'] = default_budget - amount

    with open('financials.json', 'w') as f:
        f.seek(0)

        json.dump(data, f)

def deposit(team, amount, type):
    data = g.read_Json('financials.json')

    default_budget = 0

    if type.lower() == 't':
        for i in range(len(data['teams'])):
            if data['teams'][i]['name'].lower() == team.lower():
                default_budget = data['teams'][i]['transfer']
                break

        data['teams'][i]['transfer'] = default_budget + amount

    if type.lower() == 'f':
        for i in range(len(data['teams'])):
            if data['teams'][i]['name'].lower() == team.lower():
                default_budget = data['teams'][i]['facilities']
                break

        data['teams'][i]['facilities'] = default_budget + amount

    with open('financials.json', 'w') as f:
        f.seek(0)

        json.dump(data, f)

def update_balance():
    deposit_or_withdraw = input('Deposit or withdraw? (D/W): ').upper()
    team_name = input('Enter team name: ')

    if deposit_or_withdraw == 'D':
        type = input('Deposit to transfers or facilities budget? (T/F): ')

        amount = input('Enter deposit amount: ')
        while amount.isdigit() == False:
            print('!!!!! Please enter a number !!!!!\n')
            amount = input('Enter deposit amount: ')
            print()

        amount = int(amount)

        deposit(team_name, amount, type)
    else:
        type = input('Withdraw to transfers or facilities budget? (T/F): ')

        amount = input('Enter withdraw amount: ')
        while amount.isdigit() == False:
            print('!!!!! Please enter a number !!!!!\n')
            amount = input('Enter withdraw amount: ')
            print()

        amount = int(amount)

        withdraw(team_name, amount, type)