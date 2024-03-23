import json
import random

import generation as g
import finance as fin

def add_player():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ')

    position = input('Enter position: ').upper()

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'] == team_name:
            team = data['teams'][i]['roster']
            break

    team_position = team[position]

    name = input('Enter player name: ')

    age = input('Enter player age: ')
    while age.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        age = input('Enter player age: ')
        print()

    age = int(age)

    rating = input('Enter player rating: ')
    while rating.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        rating = input('Enter player rating: ')
        print()

    cost = int(rating)

    potential = input('Enter player potential: ')
    while potential.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        cost = input('Enter player potential: ')
        print()

    potential = int(potential)

    nationality = input('Enter player nationality: ')
    tactic = input('Enter player tactical preference: ')

    player = {
        'name': name,
        'age': age,
        'position': position,
        'rating': rating,
        'potential': potential,
        'nationality': nationality,
        'tactical_preference': tactic
    }

    team_position.append(player)

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def buy_player():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ')

    position = input('Enter position: ').upper()

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'] == team_name:
            team = data['teams'][i]['roster']
            break

    team_position = team[position]

    name = input('Enter player name: ')

    age = input('Enter player age: ')
    while age.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        age = input('Enter player age: ')
        print()

    age = int(age)

    rating = input('Enter player rating: ')
    while rating.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        rating = input('Enter player rating: ')
        print()

    rating = int(rating)

    potential = input('Enter player potential: ')
    while potential.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        potential = input('Enter player potential: ')
        print()

    potential = int(potential)

    nationality = input('Enter player nationality: ')
    tactic = input('Enter player tactical preference: ')

    cost = input('Enter player cost: ')
    while cost.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
        cost = input('Enter player cost: ')
        print()

    cost = int(cost)

    player = {
        'name': name,
        'age': age,
        'position': position,
        'rating': rating,
        'potential': potential,
        'nationality': nationality,
        'tactical_preference': tactic
    }

    team_position.append(player)

    fin.withdraw(team_name, cost, 't')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)


def buy_player_params(team_name, player_position, player_name, player_age,
                      player_rating, player_potential, player_cost, player_nationality,
                      player_tactic):
    data = g.read_Json('rosters.json')

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'] == team_name:
            team = data['teams'][i]['roster']
            break

    team_position = team[player_position]

    player = {
        'name': player_name,
        'age': player_age,
        'position': player_position,
        'rating': player_rating,
        'potential': player_potential,
        'nationality': player_nationality,
        'tactical_preference': player_tactic
    }

    team_position.append(player)

    fin.withdraw(team_name, player_cost, 't')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def sell_player_params(team_name, player_position, player_name, cost):
    data = g.read_Json('rosters.json')

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            break

    team_position = team[player_position]

    for p in team_position:
        if p['name'] == player_name:
            team_position.remove(p)

    fin.deposit(team_name, cost, 't')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def sell_player():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ')

    position = input('Enter position: ').upper()

    player_name = input('Enter player name: ')

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'] == team_name:
            team = data['teams'][i]['roster']
            break

    team_position = team[position]

    cost = input('Enter player cost: ')
    while cost.isdigit() == False:
        print('!!!!! Please enter a number !!!!!\n')
        cost = input('Enter player cost: ')
        print()

    cost = int(cost)

    for p in team_position:
        if p['name'] == player_name:
            team_position.remove(p)

    fin.deposit(team_name, cost, 't')

    with open('rosters.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def get_player(team_name):
    data = g.read_Json('rosters.json')

    name = input('Enter player name: ')

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'] == team_name:
            team = data['teams'][i]['roster']
            break

    for i in range(15):
        team_position = team[positions[i]]

        for p in team_position:
            if p['name'] == name:
                return p['name'], p['age'], p['position'], p['rating'], p['potential'], p['nationality'], p['tactical_preference']

def transfer_player():
    team_name_buying = input('Enter name of purchasing club: ')
    team_name_selling = input('Enter name of selling club: ')

    player = get_player(team_name_selling)

    cost = input('Enter player cost: ')
    while cost.isdigit() == False:
        print('!!!!! Please enter a number !!!!!\n')
        cost = input('Enter player cost: ')
        print()

    cost = int(cost)

    name = player[0]
    age = player[1]
    position = player[2]
    rating = player[3]
    potential = player[4]
    nationality = player[5]
    tactic = player[6]

    buy_player_params(team_name_buying, position, name, age, rating, potential, cost, nationality, tactic)
    sell_player_params(team_name_selling, position, name, cost)

def sign_staff():
    data = g.read_Json('staff.json')

    team_name = input('Enter team name: ').lower()

    print('Position Codes')
    print('1: DOF')
    print('2: Assistant Manager')
    print('3: Goalkeeping Coach')
    print('4: Defending Coach')
    print('5: Midfield Coach')
    print('6: Attacking Coach')
    print('7: Set Piece Coach')
    print('8: Physiotherapist')

    staff_positions = ['dof', 'assistant_manager', 'goalkeeping', 'defending',
                       'midfielder', 'attacking', 'set_pieces', 'physiotherapist']

    position = input('Enter staff position: ')
    while position.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 8 !!!!!\n')
        position = input('Enter player rating: ')
        print()

    position = int(position)

    position = staff_positions[position - 1]

    name = input('Enter staff name: ')

    rating = input('Enter staff rating: ')
    while rating.isdigit() == False:
        print('!!!!! Please enter a number between 0 and 5 !!!!!\n')
        rating = input('Enter staff rating: ')
        print()

    rating = int(rating)

    cost = input('Enter staff cost: ')
    while cost.isdigit() == False:
        print('!!!!! Please enter a number !!!!!\n')
        cost = input('Enter staff cost: ')
        print()

    cost = int(cost)

    staff = {
        'name': name,
        'rating': rating,
    }

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            data['teams'][i][position] = staff
            break

    fin.withdraw(team_name, cost, 't')

    with open('staff.json', 'w') as f:
        f.seek(0)
        json.dump(data, f)

def player_offers():
    data = g.read_Json('rosters.json')

    team_name = input('Enter team name: ').lower()

    team = 'team'

    for i in range(len(data['teams'])):
        if data['teams'][i]['name'].lower() == team_name:
            team = data['teams'][i]['roster']
            break

    positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB',
                 'CDM', 'LM', 'CM', 'RM', 'CAM',
                 'LW', 'CF', 'ST', 'RW']

    offers_amount = random.randint(3,10)

    for i in range(offers_amount):
        position = random.choice(positions)

        while(team[position] == []):
            position = random.choice(positions)

        team_position = team[position]
        player = random.choice(team_position)

        value = g.calculate_Value(player['age'], player['position'], player['rating'], player['potential'])

        extra = 0

        more_or_less = random.randint(1,100)

        if value <= 5:
            extra = random.randint(0,1)
            if more_or_less % 2 == 0:
                value += extra
            else:
                value -= extra

        if value > 5 and value <= 20:
            extra = random.randint(0,3)
            if more_or_less % 2 == 0:
                value += extra
            else:
                value -= extra

        if value > 20 and value <= 40:
            extra = random.randint(0,5)
            if more_or_less % 2 == 0:
                value += extra
            else:
                value -= extra

        if value > 40:
            extra = random.randint(0,10)
            if more_or_less % 2 == 0:
                value += extra
            else:
                value -= extra

        leave_string = f'{player["name"]} wants to stay at the club'
        chance_to_leave = random.randint(1,100)

        if chance_to_leave <= 8:
            leave_string = f'{player["name"]} wants to leave the club and will force a move if he has to'

        if chance_to_leave > 8 and chance_to_leave <= 25:
            leave_string = f'{player["name"]} wants to leave but is willing to wait for a good offer'

        if chance_to_leave > 25 and chance_to_leave <= 60:
            leave_string = f'{player["name"]} is indifferent to leaving or staying'

        if chance_to_leave > 60:
            leave_string = f'{player["name"]} wants to stay at the club'

        print(f'OFFER FOR: {player['position']} | {player['name']} [{player['age']}/{player['rating']}/{player['potential']}] | {player['nationality']} | {player['tactical_preference']}')
        print(f'{value}M')
        print(leave_string)
        print()
        ''' accept = input('Accept offer? (Y/N)').upper()
        if accept == 'Y':
            sell_player_params(team_name, player['position'], player['name'], value) '''






