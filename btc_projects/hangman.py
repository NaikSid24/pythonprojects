import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    'apple', 'banana', 'grape', 'orange', 'pear', 'peach', 'plum', 'berry', 'lemon', 
    'melon', 'kiwi', 'lime', 'mango', 'cherry', 'fig', 'date', 'papaya', 'guava', 
    'apricot', 'avocado', 'coconut', 'durian', 'elderberry', 'fig', 'gooseberry', 
    'honeydew', 'jackfruit', 'lychee', 'nectarine', 'olive', 'pomegranate', 
    'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon', 'blueberry', 
    'cranberry', 'currant', 'passionfruit', 'persimmon', 'pineapple', 'prune', 
    'raisin', 'tomato', 'carrot', 'lettuce', 'cabbage', 'broccoli', 'spinach', 
    'pepper', 'onion', 'garlic', 'potato', 'tomato', 'cucumber', 'celery', 
    'radish', 'beet', 'corn', 'pea', 'bean', 'chickpea', 'lentil', 'wheat', 
    'rice', 'oats', 'barley', 'quinoa', 'rye', 'spelt', 'cornmeal', 'buckwheat', 
    'almond', 'peanut', 'walnut', 'cashew', 'hazelnut', 'pecan', 'pistachio', 
    'macadamia', 'chestnut', 'pine', 'soy', 'millet', 'sesame', 'flax', 
    'poppy', 'chia', 'sunflower', 'pumpkin', 'cacao', 'coffee', 'tea', 
    'sugar', 'honey', 'chocolate', 'candy', 'cake', 'pie', 'cookie', 'brownie', 
    'muffin', 'bread', 'pasta', 'noodle', 'pizza', 'burger', 'sandwich', 'taco', 
    'burrito', 'sushi', 'omelette', 'pancake', 'waffle', 'biscuit', 'toast', 
    'jam', 'butter', 'cheese', 'milk', 'yogurt', 'cream', 'icecream', 'soup', 
    'stew', 'curry', 'salad', 'chili', 'sauce', 'gravy', 'ketchup', 'mustard', 
    'mayonnaise', 'oil', 'vinegar', 'spice', 'salt', 'pepper', 'herb', 'basil', 
    'oregano', 'thyme', 'rosemary', 'sage', 'mint', 'cilantro', 'parsley', 
    'dill', 'chive', 'fennel', 'garlic', 'ginger', 'turmeric', 'cumin', 
    'coriander', 'paprika', 'saffron', 'vanilla', 'cinnamon', 'clove', 
    'nutmeg', 'cardamom', 'peppermint', 'oregano', 'sage', 'thyme', 'rosemary', 
    'marjoram', 'basil', 'dill', 'coriander', 'fennel', 'tarragon', 'chervil', 
    'lavender', 'bay', 'curry', 'oregano', 'mint', 'savory', 'sorrel', 
    'oregano', 'tarragon', 'oregano', 'oregano', 'oregano', 'oregano', 'oregano'
]

print(logo)
random_num = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_num]

blank_list = ['_'] * len(chosen_word)
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess the letter? ").lower()

    if guess in blank_list:
        print(f"You've already guessed {guess}")
        continue
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            blank_list[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")
    
    print(" ".join(blank_list))

    if "_" not in blank_list:
        end_of_game = True
        print("You win.")
