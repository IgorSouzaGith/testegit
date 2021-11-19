stack = [20,30]
print('The stack already has values! ', stack)
x = False # x is False
while not x:  # read  while x is False
    value = int(input('write one number: '))   
    if value > 0:  # if number > 0 then x continue false 
        if(value % 2) == 0:
            x = False
            stack.append(value)
            print('Add in Stack', stack)
        elif (value % 2) == 1:
            stack.pop()
            print('Remove number of Satck!', stack)
    else: # number  = 0 then x is True, exit while
       x = True
for item in stack[::-1]:
    stack.pop(-1)
    print('Empty Stack!', stack)

print('Program end, Stack Empty!', stack)
