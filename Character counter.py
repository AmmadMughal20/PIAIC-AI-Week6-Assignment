#Program that count occurance of characters in a user entered string

input_string = input('Enter your string: ') #user string

unique_characters = set(input_string.upper()) #unique characters in user string

for i in unique_characters:
    counter = 0
    for j in input_string.upper():
        if i == j and i != ' ':
            counter+=1 
    if i != ' ':
        print(i + ':' + str(counter))    


