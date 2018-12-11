RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3
NUM_ATTRIBUTES = 4

def create_players_dict(filename):
    the_dict = {}

    def get_value_list():
        ''' Return a list of the given values'''
        a_list = [None]*NUM_ATTRIBUTES
        a_list[RANK] = int(rank)
        a_list[COUNTRY] = country
        a_list[RATING] = int(rating)
        a_list[BYEAR] = int(byear)
        return a_list

    try:
        # Open file
        file_stream = open(filename)
        # loop through the file
        for line in file_stream:
        #   Extract the name
        #   Extract the remaining data
            rank, name, country, rating, byear = line.split(';')
            lastname, firstname = name.split(',')
            country = country.strip()
        #   Save the name, remaining data as (key,value) in dict
            key = "{}{}".format(firstname,lastname).strip()
            key = key.strip()
            value_list = get_value_list()
            #value_list = [int(rank), country, int(rating), int(byear)]
            the_dict[key] = value_list
        file_stream.close()
    except FileNotFoundError:
        pass

    return the_dict

def create_countries_dict(dict_players):
    the_dict = {}

    # loop through dict_players
    for chess_player, chess_player_data in dict_players.items():
    #   Extract name and country
        country = chess_player_data[COUNTRY]
    #   Add (or append) name as a value for the country key
        if country in the_dict:
            name_list = the_dict[country]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            the_dict[country] = name_list
    return the_dict

def get_average_rating(players, dict_players):
    ''' Returns the average rating for the given players'''
    ratings = [ dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(dict_countries, dict_players):
    # loop through sorted dict_countries
    sorted_tuples = sorted(dict_countries.items())
    #   extract number of players in country
    #   compute the average rating of each country
    for country, players in sorted_tuples:
        average = get_average_rating(players, dict_players)
        print("{} ({}) ({:.1f}):".format(country, len(players), average))
    #   for each player,
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))
    #       print name and rating
    return

def print_header(header_str):
    print(header_str)
    dashes = '-'*len(header_str)
    print(dashes)

# the main program starts here

filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries_dict(dict_players)
print_header("Players by country:")
print_sorted(dict_countries, dict_players)