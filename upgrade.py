import json
import finance as fin
import generation as g

def upgrade_training():
    data = g.read_Json('facilities.json')
    financial_data = g.read_Json('financials.json')

    team_name = input("Enter your team name: ").lower()

    levels = {
        1 : 0,
        2 : 50,
        3 : 100,
        4 : 200,
        5 : 300
    }

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            training = data['teams'][i]['training']
            facilities_budget = financial_data['teams'][i]['facilities']

            print(f'Current training facilities are level {training}')
            print(f'Upgrading training facilities to level {training + 1} will cost {levels[training + 1]}M')
            print(f'The current facilities budget is {facilities_budget}M')
            cont = input('Would you like to continue with the upgrade? (Y/N) ').upper()

            if cont == 'Y':
                data['teams'][i]['training'] = training + 1
                fin.withdraw(team_name, levels[data['teams'][i]['training']], 'f')
                financial_data = g.read_Json('financials.json')
                print(f'{team_name.upper()}s training facilities are now level {training + 1}')
                print(f'{team_name.upper()}s facilities budget is now {financial_data['teams'][i]['facilities']}M')

            break

    with open('facilities.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def upgrade_youth_academy():
    data = g.read_Json('facilities.json')
    financial_data = g.read_Json('financials.json')

    team_name = input("Enter your team name: ").lower()

    levels = {
        1 : 0,
        2 : 10,
        3 : 80,
        4 : 150,
        5 : 200
    }

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            youth = data['teams'][i]['youth']
            facilities_budget = financial_data['teams'][i]['facilities']

            print(f'Current youth academy is level {youth}')
            print(f'Upgrading youth academy to level {youth + 1} will cost {levels[youth + 1]}M')
            print(f'The current facilities budget is {facilities_budget}M')
            cont = input('Would you like to continue with the upgrade? (Y/N) ').upper()

            if cont == 'Y':
                data['teams'][i]['youth'] = youth + 1
                fin.withdraw(team_name, levels[data['teams'][i]['youth']], 'f')
                financial_data = g.read_Json('financials.json')
                print(f'{team_name.upper()}s youth academy is now level {youth + 1}')
                print(f'{team_name.upper()}s facilities budget is now {financial_data['teams'][i]['facilities']}M')

            break

    with open('facilities.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def upgrade_merchandise():
    data = g.read_Json('facilities.json')
    financial_data = g.read_Json('financials.json')

    team_name = input("Enter your team name: ").lower()

    levels = {
        1 : 0,
        2 : 50,
        3 : 100,
        4 : 200,
        5 : 250
    }

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            merchandise = data['teams'][i]['merchandise']
            facilities_budget = financial_data['teams'][i]['facilities']

            print(f'Current merchandise is level {merchandise}')
            print(f'Upgrading merchandise to level {merchandise + 1} will cost {levels[merchandise + 1]}M')
            print(f'The current facilities budget is {facilities_budget}M')
            cont = input('Would you like to continue with the upgrade? (Y/N) ').upper()

            if cont == 'Y':
                data['teams'][i]['merchandise'] = merchandise + 1
                fin.withdraw(team_name, levels[data['teams'][i]['merchandise']], 'f')
                financial_data = g.read_Json('financials.json')
                print(f'{team_name.upper()}s merchandise is now level {merchandise + 1}')
                print(f'{team_name.upper()}s facilities budget is now {financial_data['teams'][i]['facilities']}M')

            break

    with open('facilities.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def upgrade_scout():
    data = g.read_Json('facilities.json')
    financial_data = g.read_Json('financials.json')

    team_name = input("Enter your team name: ").lower()

    levels = {
        1 : 0,
        2 : 50,
        3 : 100,
        4 : 200,
        5 : 300
    }

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            scout = data['teams'][i]['scout']
            facilities_budget = financial_data['teams'][i]['facilities']

            print(f'Current scout is level {scout}')
            print(f'Upgrading scout to level {scout + 1} will cost {levels[scout + 1]}M')
            print(f'The current facilities budget is {facilities_budget}M')
            cont = input('Would you like to continue with the upgrade? (Y/N) ').upper()

            if cont == 'Y':
                data['teams'][i]['scout'] = scout + 1
                fin.withdraw(team_name, levels[data['teams'][i]['scout']], 'f')
                financial_data = g.read_Json('financials.json')
                print(f'{team_name.upper()}s scout is now level {scout + 1}')
                print(f'{team_name.upper()}s facilities budget is now {financial_data['teams'][i]['facilities']}M')

            break

    with open('facilities.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def edit_stadium_capacity():
    data = g.read_Json('facilities.json')
    financial_data = g.read_Json('financials.json')

    team_name = input("Enter your team name: ").lower()

    number_of_new_seats = input('Enter number of new seats (in thousands): ')

    while number_of_new_seats.isdigit() == False:
        print('!!!!! Please enter a number !!!!!\n')
        number_of_new_seats = input('Enter number of new seats (in thousands): ')
        print()

    number_of_new_seats = int(number_of_new_seats)

    cost = number_of_new_seats * 5

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            stadium = data['teams'][i]['stadium']
            facilities_budget = financial_data['teams'][i]['facilities']

            print(f'Current stadium capacity is {stadium}')
            print(f'Upgrading stadium capacity by {number_of_new_seats * 1000} will cost {cost}M')
            print(f'The current facilities budget is {facilities_budget}M')
            cont = input('Would you like to continue with the upgrade? (Y/N) ').upper()

            if cont == 'Y':
                data['teams'][i]['stadium'] = stadium + (number_of_new_seats * 1000)
                fin.withdraw(team_name, cost, 'f')
                financial_data = g.read_Json('financials.json')
                print(f'{team_name.upper()}s stadium capacity is now {stadium + (number_of_new_seats * 1000)}')
                print(f'{team_name.upper()}s facilities budget is now {financial_data['teams'][i]['facilities']}M')

            break

    with open('facilities.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)



