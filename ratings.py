"""Restaurant rating lister."""
import sys
from random import choice

scores_dict = {}

def main_menu():
    print('Main menu:')
    print(' 1. See all ratings')
    print(' 2. Add a new restaurant')
    print(' 3. Choose a random restaurant rating')
    print(' 4. Quit')

    choice = input('> ')
    if choice == '1':
        token = tokenize(sys.argv[1])
        output(token)
        main_menu()
    elif choice == '2':
        add_restaurant_rating()
        main_menu()
    elif choice == '3':
        random_update()
    else:
        exit()

def add_restaurant_rating(restaurant = None):
    """Prompt user to add restaurant and rating
    Adds to global dictionary variable
    """
    if restaurant == None:
        restaurant = input('Restaurant name? ').strip()

    rating = None


    while True:
        try:
            while True:
                rating = int(input('Rating? ').strip())
                if rating > 0 and rating <= 5:
                    break
                else:
                    print('Must be between 1 and 5')
                    continue
        except:
            print('Must be 1 - 5')
            continue
        else:
            scores_dict[restaurant] = rating
            break


def tokenize(filename):
    """Split restaurant names into resaturant:score pairs
    Returns a dictionary object
    """
    
    scores = open(filename)

    for line in scores:
        split_lst = line.strip().split(':')
        scores_dict[split_lst[0]] = split_lst[1]

    return scores_dict

def output(dict):
    """Output sorted restaurants to terminal"""
    
    for restaurant, rating in sorted(dict.items()):
        print(f'{restaurant} is rated at {rating}.')

def random_update():
    token = tokenize(sys.argv[1])
    lst = []
    for item in sorted(token.items()):
        lst.append(item)
    
    random_restaurant = choice(lst)
    print(f'{random_restaurant[0]} is rated at {random_restaurant[1]}.')

    update_rating = input('Update Rating? (y/n)')
    if update_rating.lower() == 'y' or update_rating.lower() == 'yes':
        add_restaurant_rating(random_restaurant[0])
        output(scores_dict)
        main_menu()
        

# random_update()
main_menu()
