"""Restaurant rating lister."""

restaurant_rating_dict = {}

def reading_ratings(restaurant_file):

    for line in open(restaurant_file):
        each_restaurant = line.split(':')
        restaurant_name = each_restaurant[0].strip()
        restaurant_rating = int(each_restaurant[1].strip())

        restaurant_rating_dict[restaurant_name] = restaurant_rating

def add_restaurant_rating():
    
    new_restaurant_name = input("Please enter restaurant name:")

    while True:

        new_restaurant_rating = input("Please enter rating (1-5): ")
        new_restaurant_rating = int(new_restaurant_rating)

        if new_restaurant_rating < 6:
            print()
            break
        else: 
            print("Please enter a number between 1 and 5.")



    restaurant_rating_dict[new_restaurant_name] = new_restaurant_rating


def sort_restaurant_alphabetically():
    for restaurant_name, restaurant_rating in sorted(restaurant_rating_dict.items()):
        print(f'{restaurant_name} is rated at {restaurant_rating}.')

def options_for_restaurant_ratings():
    
    reading_ratings('scores.txt')
    
    while True:
        print(
        '''Here are your options:
            Type "A" if you would like to add a restaurant
                 "S" if you would like to see the rating
                 "Q" to quit''')

        action_choice = input('>')

        if action_choice == 'A':
            add_restaurant_rating()
        elif action_choice == 'S':
            sort_restaurant_alphabetically()
        elif action_choice == 'Q':
            print("bye")
            break
        else:
            print("Invalid choice. Please choose again.")