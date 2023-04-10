"""Restaurant rating lister."""
import sys

scores_dict = {}

def add_restaurant_rating():
    """Prompt user to add restaurant and rating
    Adds to global dictionary variable
    """

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


add_restaurant_rating()
token = tokenize(sys.argv[1])
output(token)

