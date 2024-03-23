import generation as g

if __name__ == '__main__':
    print('Welcome to the EWFL Scouting Hub')

    data = g.read_Json('countries.json')

    cont = 'y'

    while cont == 'y' or cont == 'Y':
        type = input('Scout competition or team? (C/T): ').upper()
        country = input('Enter country you wish to scout: ').upper()
        scout_level = input('Enter your scout level: ')
        scout_level = int(scout_level)
        position = input('Enter player position: ')
        preferred_tactic = input('Enter preferred tactic: ')

        if type == 'C':
            for i in range(5):
                player = g.generate_Player(data, country, scout_level, position, preferred_tactic)

                if player[5]:
                    print('*** Hidden Gem ***')
                print(f'Age: {player[0]}')
                print(f'Position: {player[1]}')
                print(f'Rating: {player[2]}')
                print(f'Potential: {player[3]}')
                print(f'Tactic: {player[6]}')
                print(f'Value: {player[4]}M\n')

            cont = input("Continue? (Y/N): ")
            print()

        if type == 'T':
            rating = input('Enter team rating: ')
            print()

            while rating.isdigit() == False:
                print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
                rating = input('Enter scout level: ')
                print()

            rating = int(rating)

            while rating < 1 or rating > 99:
                print('!!!!! Please enter a number between 1 and 99 !!!!!\n')
                rating = input('Enter scout level: ')
                print()
                if rating.isdigit():
                    rating = int(rating)

            player = g.generate_Player_From_Team(rating)

            print()
            if player[5]:
                print('*** Hidden Gem ***')
            print(f'Age: {player[0]}')
            print(f'Position: {player[1]}')
            print(f'Rating: {player[2]}')
            print(f'Potential: {player[3]}')
            print(f'Value: {player[4]}M\n')

            cont = input("Continue? (Y/N): ")
            print()