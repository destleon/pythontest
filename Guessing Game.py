correct_year = 1994

while True:
    user_input = int(input('When was Python 1.0 released? '))

    if user_input == correct_year:
        print('Correct!')
        break
    elif user_input < correct_year:
        print('It was later than that!')
    else:
        print('It was earlier than that!')