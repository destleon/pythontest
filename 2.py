sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        print('Bye!')
        break
    
    elif user_input in sample_dict:
        translation = sample_dict[user_input]
        print('Translation:', translation)
    
    else:
        print('No match')