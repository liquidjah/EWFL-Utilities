import json
import generation as g
import finance as fin
import random

def edit_names():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ').lower()

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            break

    for x in range(len(team)):
        position = team[positions[x]]
        for y in position:
            print(positions[x], y['name'],'[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')
            default_name = y['name']
            name = input('Enter new name: ')
            if name == '':
                name = default_name
            y['name'] = name
            print('NEW NAME:',positions[x], y['name'],
                  '[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def edit_ratings_and_potentials():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ').lower()

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            break

    for x in range(len(team)):
        position = team[positions[x]]
        for y in position:
            print(positions[x], y['name'],'[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')
            default_rating = y['rating']
            default_potential = y['potential']
            rating = input('Enter new rating: ')
            potential = input('Enter new potential: ')
            if rating == '' or rating.isdigit() == False:
                rating = default_rating
            if potential == '' or potential.isdigit() == False:
                potential = default_potential
            y['rating'] = rating
            y['potential'] = potential
            print('NEW OVR/POT:',positions[x], y['name'],
                  '[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def update_ages():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ').lower()

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            break

    for x in range(len(team)):
        position = team[positions[x]]
        for y in position:
            print(positions[x], y['name'],'[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')
            default_age = int(y['age'])
            y['age'] = default_age + 1
            print('NEW AGE:',positions[x], y['name'],
                  '[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def training_upgrades():
    data = g.read_Json('rosters.json')
    facilities_data = g.read_Json('facilities.json')

    team_name = input('Enter team name: ').lower()

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            training_level = facilities_data['teams'][i]['training']
            break

    for x in range(len(team)):
        position = team[positions[x]]
        for y in position:
            print(positions[x], y['name'],'[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')
            default_rating = int(y['rating'])
            default_potential = int(y['potential'])
            extra_rating = 0
            extra_potential = 0
            luck = random.randint(1,100)
            if training_level > 0:
                extra_rating = random.randint(0, training_level)
                extra_potential = random.randint(0, training_level)
                if luck > 95:
                    extra_potential *= 2
            y['rating'] = default_rating + extra_rating
            y['potential'] = default_potential + extra_potential
            if y['rating'] > y['potential']:
                y['potential'] = y['rating']
            print('NEW RATING:',positions[x], y['name'],
                  '[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)