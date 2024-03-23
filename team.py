import generation as g
import edit as e
import get_data as gd
import transfer as t
import finance as fin
import upgrade as u
import random
import json

if __name__ == '__main__':
    print('Welcome to the EWFL Team Hub')

    team_data = g.read_Json('rosters.json')

    cont = 'y'

    while cont == 'y' or cont == 'Y':
        print('EWFL Team Hub Codes')
        print('G: Generate new team')
        print('A: Add player')
        print('S: Sell player')
        print('B: Buy player')
        print('T: Transfer player')
        print('UB: Update team balance')
        print('EN: Edit player names')
        print('ER: Edit player ratings/potentials')
        print('UA: Update ages')
        print('ATU: Apply training upgrades')
        print('UT: Upgrade training facilities')
        print('UY: Upgrade youth academy')
        print('UM: Upgrade merchandise')
        print('US: Upgrade scout')
        print('UST: Upgrade stadium')
        print('P: See teams')
        print('FN: See financials')
        print('ST: See staff')
        print('F: See facilities')
        print('O: See offers')
        print()

        type = input('What would you like to do? ').upper()

        if type == 'P':
            gd.print_Teams()

        if type == 'FN':
            gd.print_Financials()

        if type == 'F':
            gd.print_Facilities()

        if type == 'ST':
            gd.print_Staff()

        if type == 'SS':
            t.sign_staff()

        if type == 'A':
            t.add_player()

        if type == 'B':
            t.buy_player()

        if type == 'S':
            t.sell_player()

        if type == 'T':
            t.transfer_player()

        if type == 'UB':
            fin.update_balance()

        if type == 'EN':
            e.edit_names()

        if type == 'ER':
            e.edit_ratings_and_potentials()

        if type == 'UA':
            e.update_ages()

        if type == 'ATU':
            e.training_upgrades()

        if type == 'UT':
            u.upgrade_training()

        if type == 'UY':
            u.upgrade_youth_academy()

        if type == 'UM':
            u.upgrade_merchandise()

        if type == 'US':
            u.upgrade_scout()

        if type == 'UST':
            u.edit_stadium_capacity()

        if type == 'O':
            t.player_offers()

        if type == 'G':
            team_name = input('Enter team name: ')

            current_team = team_name

            team = {
                'name': team_name,
                'roster' : {
                    'GK' : [],
                    'LWB': [],
                    'LB' : [],
                    'CB': [],
                    'RB' : [],
                    'RWB': [],
                    'CDM': [],
                    'LM': [],
                    'CM': [],
                    'RM' : [],
                    'CAM': [],
                    'LW' : [],
                    'CF' : [],
                    'ST': [],
                    'RW': [],
                }
            }

            finance = {
                'name': team_name,
                'transfer' : 0,
                'facilities' : 0,
            }

            facilities = {
                'name': team_name,
                'stadium' : 1000,
                'training' : 1,
                'youth' : 1,
                'merchandise' : 1,
                'scout' : 1
            }

            staff = {
                'name': team_name,
                'dof' : {
                    'name' : 'none',
                    'rating' : 0
                },
                'assistant_manager' : {
                    'name': 'none',
                    'rating': 0,
                },
                'goalkeeping' : {
                    'name': 'none',
                    'rating': 0
                },
                'defending' : {
                    'name': 'none',
                    'rating': 0
                },
                'midfielder' : {
                    'name': 'none',
                    'rating': 0
                },
                'attacking' : {
                    'name': 'none',
                    'rating': 0
                },
                'set_pieces' : {
                    'name': 'none',
                    'rating': 0
                },
                'physiotherapist' : {
                    'name': 'none',
                    'rating': 0
                }
            }

            with open('rosters.json', 'r+') as f:
                team_data = json.load(f)

                team_data['teams'].append(team)

                current_team = len(team_data['teams']) - 1

                f.seek(0)

                json.dump(team_data, f)

            with open('financials.json', 'r+') as f:
                team_data = json.load(f)

                team_data['teams'].append(finance)

                f.seek(0)

                json.dump(team_data, f)

            with open('facilities.json', 'r+') as f:
                team_data = json.load(f)

                team_data['teams'].append(facilities)

                f.seek(0)

                json.dump(team_data, f)

            with open('staff.json', 'r+') as f:
                team_data = json.load(f)

                team_data['teams'].append(staff)

                f.seek(0)

                json.dump(team_data, f)


            print(f'Welcome to EWFL {team_name}')
            print()
            rating = input('Enter team rating: ')
            print()

            while rating.isdigit() == False:
                print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
                rating = input('Enter team rating: ')
                print()

            rating = int(rating)

            while rating < 1 or rating > 99:
                print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
                rating = input('Enter team rating: ')
                print()
                if rating.isdigit():
                    rating = int(rating)

            player_ratings = g.generate_Team_Ratings(rating)
            player_ages = g.generate_Ages()

            formations = ['3-4-3', '3-5-2', '4-4-2', '4-2-3-1', '4-3-3', '4-5-1',
                          '4-2-2-2', '4-2-4', '4-4-1-1', '4-1-2-1-2', '5-3-2', '5-2-3', '5-4-1',
                          '5-2-1-2']

            print('Formations')
            for f in range(len(formations)):
                print(f'{f+1}: {formations[f]}')

            formation = input('Enter team formation: ')
            print()

            while formation.isdigit() == False:
                print('!!!!! Please enter a number between 1 and 14 !!!!!\n')
                formation = input('Enter team formation: ')
                print()

            formation = int(formation) - 1

            while formation < 1 or formation > 14:
                print('!!!!! Please enter a number between 1 and 14 !!!!!\n')
                formation = input('Enter team formation: ')
                print()
                if formation.isdigit():
                    formation = int(formation) - 1

            positions = g.generate_Positions(formations[formation])

            country_of_origin = input('Enter country of origin: ')
            print()
            tactical_preference = input('Enter tactical preference: ')
            preferred_tactics = g.generate_Preferred_Tactics(tactical_preference)
            print()

            for i in range(23):
                player_name = 'player ' + str(i + 1)
                player = {
                    'name': player_name,
                    'age': player_ages[i],
                    'position': positions[i % len(positions)],
                    'rating': player_ratings[i],
                    'potential': g.set_Potential(player_ages[i], player_ratings[i]),
                    'nationality': country_of_origin,
                    'tactical_preference': preferred_tactics[i]
                }

                with open('rosters.json', 'r+') as f:
                    team_data = json.load(f)

                    team_data['teams'][current_team]['roster'][positions[i % len(positions)]].append(player)

                    f.seek(0)

                    json.dump(team_data, f)


        print()

        cont = input("Continue? (Y/N): ")
        print()