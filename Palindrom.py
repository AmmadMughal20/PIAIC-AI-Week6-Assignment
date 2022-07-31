#Program that count occurance of characters in a user entered string

input_string = input('Enter your string: ').upper() #user string
inverse_string = input_string[::-1]
print('It is palindrom.') if input_string == inverse_string else print('Not a palindrom.')
    

    
    

