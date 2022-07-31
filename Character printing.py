#Program to print 
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

user_input = int(input('Enter your number: '))

list_to_print = []

for i in range(0, user_input):
    list_to_print.append(str(i+1))

while list_to_print:
    string_val = ' '.join(list_to_print)
    print(string_val)
    del list_to_print[len(list_to_print)-1]