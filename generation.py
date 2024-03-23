import random
import json
from functools import reduce

def read_Json(file):
    f = open(file)
    data = json.load(f)

    return data


def calculate_Value(age, position, rating, potential):
    value = 0
    if rating < 60:
        value = random.randint(0, 1)

    if rating >= 60 and rating <= 65:
        value = random.randint(1, 3)

    if rating > 65 and rating <= 70:
        value = random.randint(3, 8)

    if rating > 70 and rating <= 75:
        value = random.randint(8, 12)

    if rating > 75 and rating <= 80:
        value = random.randint(12, 25)

    if rating > 80 and rating <= 83:
        value = random.randint(25, 35)

    if rating > 83 and rating <= 86:
        value = random.randint(35, 60)

    if rating > 86 and rating <= 88:
        value = random.randint(60, 90)

    if rating > 88 and rating <= 90:
        value = random.randint(90, 120)

    if rating > 90:
        value = random.randint(150, 250)

    if age > 23 and age <= 26:
        value -= (value * 0.2)

    if age > 26 and age <= 29:
        value -= (value * 0.3)

    if age > 29:
        value -= (value * 0.5)

    if age < 25 and rating > 82:
        value += (36 - age) * 2

    if age < 23:
        value += (potential - rating) * 2
    if age > 23 and age < 30:
        value += (potential - rating) * 1.5
    else:
        value += (potential - rating)

    position = position.upper()

    if position == 'GK' or position == 'LB' or position == 'CB' or position == 'RB':
        value -= (value * 0.3)

    if rating < 60:
        value = random.randint(0, 2)

    return value


def set_Age():
    return random.randint(16, 35)


def set_Potential(age, rating):
    potential = 0

    extra = 0
    luck = random.randint(1, 100)
    if luck > 70:
        luck = random.randint(1, 100)
        if luck <= 5:
            extra = random.randint(5, 10)
        if luck > 5 and luck <= 25:
            extra = random.randint(3, 8)
        if luck > 25 and luck <= 50:
            extra = random.randint(2, 7)
        if luck > 50 and luck <= 80:
            extra = random.randint(1, 5)
        if luck > 80:
            extra = random.randint(0, 3)

    if age <= 19:
        potential = random.randint(rating + 1, rating + 20) - extra

    elif age > 19 and age <= 23:
        potential = random.randint(rating + 1, rating + 15) - extra

    elif age > 23 and age <= 26:
        potential = random.randint(rating + 1, rating + 10) - extra

    elif age > 26 and age <= 29:
        potential = random.randint(rating + 1, rating + 5) - extra

    elif age > 29 and age <= 31:
        potential = random.randint(rating + 1, rating + 2) - extra

    elif age > 31:
        potential = rating

    if potential < rating:
        potential = rating

    if potential > 99:
        potential = 99

    return potential


def set_Player_Quality(data, country, scout_Level):
    exists = False
    print()

    for i in data:
        if i['code'] == country:
            exists = True

    while exists == False:
        print(f'!!!!! Country "{country}" does not exist, please enter valid country !!!!!\n')
        country = input('Enter country you wish to scout: ').upper()
        print()

        for i in data:
            if i['code'] == country:
                exists = True

    for i in data:
        if i['code'] == country:
            player_Quality = ((random.randint(i['youth'][0], i['youth'][1]) * scout_Level) / 99) + (i['youth'][2] / 99)

    if player_Quality > 5:
        player_Quality = 5

    if player_Quality < 0.1:
        player_Quality = 0.1

    return player_Quality, scout_Level


def set_Player_Quality_From_Team(team_Rating):
    scout_Level = input('Enter scout level: ')
    print()

    while scout_Level.isdigit() == False:
        print('!!!!! Please enter a number between 1 and 5 !!!!!\n')
        scout_Level = input('Enter scout level: ')
        print()

    scout_Level = int(scout_Level)

    while scout_Level != 1 and scout_Level != 2 and scout_Level != 3 and scout_Level != 4 and scout_Level != 5:
        print('!!!!! Please enter a number between 1 and 5 !!!!!\n')
        scout_Level = input('Enter scout level: ')
        print()
        if scout_Level.isdigit():
            scout_Level = int(scout_Level)

    if scout_Level == 1:
        player_Quality = ((random.randint(team_Rating - 20, team_Rating + 3) * scout_Level) / 99) + (team_Rating / 99)

    if scout_Level == 2:
        player_Quality = ((random.randint(team_Rating - 15, team_Rating + 3) * scout_Level) / 99) + (team_Rating / 99)

    if scout_Level == 3:
        player_Quality = ((random.randint(team_Rating - 10, team_Rating + 4) * scout_Level) / 99) + (team_Rating / 99)

    if scout_Level == 4:
        player_Quality = ((random.randint(team_Rating - 8, team_Rating + 5) * scout_Level) / 99) + (team_Rating / 99)

    if scout_Level == 5:
        player_Quality = ((random.randint(team_Rating - 5, team_Rating + 5) * scout_Level) / 99) + (team_Rating / 99)

    if player_Quality > 5:
        player_Quality = 5

    if player_Quality < 0.1:
        player_Quality = 0.1

    return player_Quality, scout_Level

def set_Player_Rating(player_Quality, age, scout_Level):
    if player_Quality <= 0.1:
        player_Rating = random.randint(10, 49)
    if player_Quality > 0.1 and player_Quality <= 0.5:
        player_Rating = random.randint(50, 55)
    if player_Quality > 0.5 and player_Quality <= 1:
        player_Rating = random.randint(56, 60)
    if player_Quality > 1 and player_Quality <= 1.5:
        player_Rating = random.randint(61, 65)
    if player_Quality > 1.5 and player_Quality <= 2:
        player_Rating = random.randint(66, 70)
    if player_Quality > 2 and player_Quality <= 2.5:
        player_Rating = random.randint(71, 75)
    if player_Quality > 2.5 and player_Quality <= 3:
        player_Rating = random.randint(76, 80)
    if player_Quality > 3 and player_Quality <= 3.5:
        player_Rating = random.randint(81, 85)
    if player_Quality > 3.5 and player_Quality <= 4:
        player_Rating = random.randint(86, 90)
    if player_Quality > 4 and player_Quality <= 4.5:
        player_Rating = random.randint(91, 95)
    if player_Quality > 4.5:
        player_Rating = random.randint(96, 99)

    hidden_Gem = random.randint(1, 100)
    hidden_gem_bool = False

    if scout_Level == 1:
        if hidden_Gem > 98:
            if player_Rating < 70:
                player_Rating += 20
            if player_Rating >= 70 and player_Rating <= 85:
                player_Rating += 10
            if player_Rating > 85:
                player_Rating += 8

            hidden_gem_bool = True

    if scout_Level == 2:
        if hidden_Gem > 96:
            if player_Rating < 70:
                player_Rating += 20
            if player_Rating >= 70 and player_Rating <= 85:
                player_Rating += 10
            if player_Rating > 85:
                player_Rating += 8

            hidden_gem_bool = True

    if scout_Level == 3:
        if hidden_Gem > 94:
            if player_Rating < 70:
                player_Rating += 20
            if player_Rating >= 70 and player_Rating <= 85:
                player_Rating += 10
            if player_Rating > 85:
                player_Rating += 8

            hidden_gem_bool = True

    if scout_Level == 4:
        if hidden_Gem > 92:
            if player_Rating < 70:
                player_Rating += 20
            if player_Rating >= 70 and player_Rating <= 85:
                player_Rating += 10
            if player_Rating > 85:
                player_Rating += 8

            hidden_gem_bool = True

    if scout_Level == 5:
        if hidden_Gem > 90:
            if player_Rating < 70:
                player_Rating += 20
            if player_Rating >= 70 and player_Rating <= 85:
                player_Rating += 10
            if player_Rating > 85:
                player_Rating += 8

            hidden_gem_bool = True

    if player_Rating > 99:
        player_Rating = 99

    if player_Rating > 93:
        down = random.randint(0,100)

        if down > 10:
            player_Rating -= random.randint(5, 10)

    if age <= 19 and player_Rating > 83:
        player_Rating = 83

    if age > 19 and age <= 23 and player_Rating > 88:
        player_Rating = 88

    if player_Rating < 77:
        hidden_Gem = False

    return player_Rating, hidden_gem_bool

def set_player_tactic(scout_level, preferred_tactic):
    tactics = ['Gegennaccio', 'Catenaccio', 'Route One', 'Counter Attacking', 'Balanced', 'Control Possession',
               'Tiki-Taka', 'Gegenpress', 'Wing Play']

    luck = random.randint(0,100)

    if scout_level == 1:
        if luck > 90:
            return preferred_tactic
        else:
            return random.choice(tactics)
    if scout_level == 2:
        if luck > 80:
            return preferred_tactic
        else:
            return random.choice(tactics)
    if scout_level == 3:
        if luck > 70:
            return preferred_tactic
        else:
            return random.choice(tactics)
    if scout_level == 4:
        if luck > 60:
            return preferred_tactic
        else:
            return random.choice(tactics)
    if scout_level == 5:
        if luck > 50:
            return preferred_tactic
        else:
            return random.choice(tactics)

def generate_Player(data, country, scout_level, player_Position, preferred_tactic):
    player_Age = set_Age()
    player_Quality = set_Player_Quality(data, country, scout_level)
    player = set_Player_Rating(player_Quality[0], player_Age, player_Quality[1])
    player_Rating = player[0]
    hidden_Gem = player[1]
    player_tactic = set_player_tactic(scout_level, preferred_tactic)
    player_Potential = set_Potential(player_Age, player_Rating)
    player_Value = calculate_Value(player_Age, player_Position, player_Rating, player_Potential)

    return player_Age, player_Position, player_Rating, player_Potential, player_Value, hidden_Gem, player_tactic

def generate_Player_From_Team(team_Rating):
    player_Age = set_Age()
    player_Quality = set_Player_Quality_From_Team(team_Rating)
    player = set_Player_Rating(player_Quality[0], player_Age, player_Quality[1])
    player_Rating = player[0]
    hidden_Gem = player[1]
    player_Position = input("Enter position: ")
    player_Potential = set_Potential(player_Age, player_Rating)
    player_Value = calculate_Value(player_Age, player_Position, player_Rating, player_Potential)

    return player_Age, player_Position, player_Rating, player_Potential, player_Value, hidden_Gem

def generate_Team_Ratings(team_Rating):
    while True:
        l = [random.randint(40,60) for i in range(23)]
        avg = reduce(lambda x, y: x + y, l) / len(l)

        if avg == team_Rating:
            return l
def generate_Ages():
    ages = [random.randint(16, 35) for i in range(23)]
    return ages

def generate_Preferred_Tactics(preferred_tactic):
    tactics = ['Gegennaccio', 'Catenaccio', 'Route One', 'Counter Attacking', 'Balanced', 'Control Possession',
               'Tiki-Taka', 'Gegenpress', 'Wing Play']
    preferred_tactics = [random.randint(1, 100) for i in range(23)]

    for i in range(len(preferred_tactics)):
        if preferred_tactics[i] > 30:
            preferred_tactics[i] = preferred_tactic
        else:
            preferred_tactics[i] = random.choice(tactics)

    return preferred_tactics

def generate_Positions(formation):
    positions_by_formations = {
        '3-4-3': ['GK', 'CB', 'CB', 'CB',
                  'LM', 'CM', 'CM', 'RM',
                  'ST', 'ST', 'ST'],
        '3-5-2': ['GK', 'CB', 'CB', 'CB',
                  'LM', 'CM', 'CDM', 'CM', 'RM',
                  'ST', 'ST'],
        '4-4-2': ['GK', 'LB', 'CB', 'CB', 'RB',
                  'LM', 'CM', 'CM', 'RM',
                  'ST', 'ST', 'ST'],
        '4-2-3-1': ['GK', 'LB', 'CB', 'CB', 'RB',
                    'CM', 'CM',
                    'LW', 'CAM', 'RW',
                    'ST'],
        '4-3-3': ['GK', 'LB', 'CB', 'CB', 'RB',
                  'CM', 'CM', 'CM',
                  'LW', 'ST', 'RW'],
        '4-5-1': ['GK', 'LB', 'CB', 'CB', 'RB',
                  'LM', 'CM', 'CDM', 'CM', 'RM',
                  'ST'],
        '4-2-2-2': ['GK', 'LB', 'CB', 'CB', 'RB',
                    'CDM', 'CDM',
                    'CAM', 'CAM',
                    'ST', 'ST'],
        '4-2-4': ['GK', 'LB', 'CB', 'CB', 'RB',
                  'CM', 'CM',
                  'LW', 'ST', 'ST', 'RW'],
        '4-4-1-1': ['GK', 'LB', 'CB', 'CB', 'RB',
                    'LM', 'CM', 'CM', 'RM',
                    'CAM',
                    'ST'],
        '4-1-2-1-2': ['GK', 'LB', 'CB', 'CB', 'RB',
                      'CM', 'CDM', 'CM',
                      'CAM',
                      'ST', 'ST'],
        '5-3-2': ['GK', 'LWB', 'CB', 'CB', 'CB', 'RWB',
                  'CM', 'CM', 'CM',
                  'ST', 'ST'],
        '5-2-3': ['GK', 'LWB', 'CB', 'CB', 'CB', 'RWB',
                  'CM', 'CM',
                  'LW', 'ST', 'RW'],
        '5-4-1': ['GK', 'LWB', 'CB', 'CB', 'CB', 'RWB',
                  'LM', 'CM', 'CM', 'RM',
                  'ST'],
        '5-2-1-2': ['GK', 'LWB', 'CB', 'CB', 'CB', 'RWB',
                    'CM', 'CM',
                    'CAM',
                    'ST', 'ST']
    }

    return positions_by_formations[formation]