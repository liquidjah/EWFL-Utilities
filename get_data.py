import generation as g
import edit as e
import finance as fin
import random

def print_Teams():
    data = g.read_Json('rosters.json')

    data = data['teams']

    counter = 0

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    for i in range(len(data)):
        print(data[i]['name'])
        team = data[i]['roster']
        for x in range(15):
            position = data[i]['roster'][positions[x]]
            for y in position:
                print(positions[x], '|', y['name'], '|', '[' + str(y['age']) + '/' + str(y['rating']) + '/' + str(y['potential']) + ']', '|', y['nationality'], '|', y['tactical_preference'])
        counter += 1
        print()

def print_Financials():
    data = g.read_Json('financials.json')

    data = data['teams']

    counter = 0

    for i in range(len(data)):
        print(data[i]['name'])
        print('Transfer Budget:', str(data[i]['transfer']) + 'M')
        print('Facilities Budget:', str(data[i]['facilities']) + 'M')
        counter += 1
        print()

def print_Facilities():
    data = g.read_Json('facilities.json')

    data = data['teams']

    counter = 0

    for i in range(len(data)):
        print(data[i]['name'])
        print('Stadium Capacity:', str(data[i]['stadium']))
        print('Training Facilities:', str(data[i]['training']))
        print('Youth Academy:', str(data[i]['youth']))
        print('Scout:', str(data[i]['scout']))
        print('Merchandise:', str(data[i]['merchandise']))
        counter += 1
        print()

def print_Staff():
    data = g.read_Json('staff.json')

    data = data['teams']

    counter = 0

    for i in range(len(data)):
        print(data[i]['name'])
        print('Director of Football Operations:', data[i]['dof']['name'], '|', str(data[i]['dof']['rating']))
        print('Assistant Manager:', data[i]['assistant_manager']['name'], '|' , str(data[i]['assistant_manager']['rating']))
        print('Goalkeeping Coach:', data[i]['goalkeeping']['name'], '|', str(data[i]['goalkeeping']['rating']))
        print('Defending Coach:', data[i]['defending']['name'], '|', str(data[i]['defending']['rating']))
        print('Midfield Coach:', data[i]['midfielder']['name'], '|', str(data[i]['midfielder']['rating']))
        print('Attacking Coach:', data[i]['attacking']['name'], '|', str(data[i]['attacking']['rating']))
        print('Set Piece Coach:', data[i]['set_pieces']['name'], '|', str(data[i]['set_pieces']['rating']))
        print('Physiotherapist:', data[i]['physiotherapist']['name'], '|', str(data[i]['physiotherapist']['rating']))
        counter += 1
        print()