#Program to print
#    5
#   4 4
#  3   3
# 2     2
#1       1
# 2     2
#  3   3
#   4 4
#    5

input_number = int(input('Enter your string: ')) #user string

for i in range(1, input_number+1):
    for j in range(1,input_number-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print(input_number-i+1, end="")
        else:
            print(" ", end="")
    print()

counter = 2
for i in range(input_number-1, 0, -1):
    for j in range(1,input_number-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print(counter, end="")
        else:
            print(" ", end="")
    counter += 1    
    print()