#Program that count occurance of characters in a user entered string

input_string = input('Enter your string: ') #user string

unique_characters = set(input_string.upper()) #unique characters in user string

vowels, consonants = 0, 0

for i in unique_characters:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U': 
        vowels += 1 
    elif i == ' ':
        pass
    else:
        consonants += 1

print('Vowels: ' + str(vowels) + '\n' + 'Consonants: ' + str(consonants))
        
