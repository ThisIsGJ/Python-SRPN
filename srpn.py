#!/usr/bin/env python
#created  by Jun Guan (User Name:jg495)

#LIBRARY IMPORT
import re                                     #use re.split function 
import string
import sys

#GLOBAL VARIABLE
global stack                                #used to store value from user 
stack = []
global max_value                         #the maximum value for output
max_value = 2147483647
global min_value                        #the minimum value for output 
min_value = -2147483648
global answer
answer = 0
global random_times
random_times = 0
global random_list
#creat a list to minic the random number generatoe
random_list = [ 1562469902 , 1039845534 , 2025653534 , 739593874 , 994290584 ,
1198075102 , 605335584 , 563009619 , 1076425455 , 1979353639 , 1481705266 ,
416282717 , 1502074844 , 339011283 , 1656724019 , 75412011 , 296441807 ,
1150973001 , 1935872936 , 378814183 , 1318686473 , 2034028701 , 1310947874,
2095686658,1548890542,987301502,543737933,1987654433,111092794,1359561819,
1253077815,1673562696,251923705,1131247701,265672923,1246214289,181839156,
871008507,1809223908,1258264611,702878498,1143445526,1674547328,57469695,
1482456809]

#main operation function
def main_operation():
    global stack
    global answer
    global max_value
    global min_value
    global random_time
            
    number = raw_input("")
    input_list = re.split('([^0-9])', number)
    if input_list[0] == '' and input_list[1] == '-' and input_list[2] != '':
        input_list = string.split(number)
    # used to restrict the stack length
    elif len(stack) > 22:
        try:#if the input is operater it will go to except
            number = int(number) 
            sys.stderr.write('Stack overflow.\n')
            main_operation()
        except:
            pass
        
    for element in input_list:
        if element == '#': #used for comment
            break 
        
        elif element == '' or element == ' ':
            continue
        #basic operation
        elif element == '+' or element == '-' or element == '*' or element == '/' or element =='%' or element == '^' :
            basic_operation(element)
        #display stack
        elif element == 'd':
            for i in stack:
                print i 
        #generate random number for random list
        elif element == 'r':
            if len(stack) < 23:
                element = random_number(element)
                if element == 'Stack overflow.':
                    sys.stderr.write('Stack overflow.\n')
                else:
                    append_into_stack(element)
            else:
                sys.stderr.write("Stack overflow.\n")    
        elif element == '=':
            print stack[-1]
            
        else:
            append_into_stack(element)
        
    main_operation()


# basic function for '+' '-' '*' '/' '%' 
def basic_operation(element):
    global stack
    global answer
    try:
        if element == '+':
            answer = stack.pop()+stack.pop()
            #give the maximum or minimum value if the answer saturate
            answer = checkValue(answer)
            stack.append(answer)
            
        elif element == '-':
            answer = -stack.pop()+stack.pop()
            answer = checkValue(answer)
            stack.append(answer)
                    
        elif element == '*':
            answer = stack.pop()*stack.pop()
            answer = checkValue(answer)
            stack.append(answer)
                    
        elif element == '/':
            if stack[-1] == 0:
                sys.stderr.write('Divide by 0.\n')
            else:
                if stack[-1]*stack[-2] < 0:
                    answer = -(-stack.pop(-2)/stack.pop())
                else:    
                    answer = stack.pop(-2)/stack.pop()
            answer = checkValue(answer)
            stack.append(answer)
                
        elif element == '%':
            if stack[-2]*stack[-1] < 0:
                answer = -(stack.pop(-2) % stack.pop())
            else:
                answer = stack.pop(-2) % stack.pop()
                answer = checkValue(answer)
            stack.append(answer)
    
        elif element == '^':
            answer = stack.pop(-2)**stack.pop()
            answer = int(answer)
            answer = checkValue(answer)
            stack.append(answer)
            
    except:
        sys.stderr.write('Stack underflow.\n')
        return 0
                
def checkValue(i):#check whether the answer saturate
    global max_value, min_value
    if i > max_value:
        i = max_value
    elif i < min_value:
        i = min_value
    return i
    
def append_into_stack(i):
    try:
        return stack.append(int(i))
    except:
        sys.stderr.write("Unrecognised operator or operand \"" + str(i) + "\". \n")
        
def random_number(i):#used for symbol 'r'
    global random_list
    global random_times

    if random_times == 23:
        random_times = 0
        
    try:
        i = random_list[random_times]
        random_times += 1
        return i
    except :
        i = 'Stack overflow.'
        return i
                    
while(True):
    try:
        main_operation()
    except:
        break        

                        
                        
                        
                        
