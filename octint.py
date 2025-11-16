#check if valid octinteger using nfa approach

#boolean function to check if oct integer
#cannot use int, float, s.isdigit, regex libraries
#can use for/while, if else, <= ‘0-9’

def is_octint(s):

    ##if the length of input string is 0, return False
    if len(s) == 0:
        return False
    state = 'q1'

    ##loop through each character in the string
    for char in s:

        if state == 'q1':
            #first state must be 0
            if char == '0':
                state = 'q2'
            else:
                return False
            
        elif state == 'q2':
            #second state must be 'o' or 'O'
            if char == 'o' or char == 'O':
                state = 'q3'
            else:
                return False

        elif state == 'q3':
            ##fourth state: check if character is a digit 0-7
            if '0' <= char <= '7':
                state = 'q3'
            ##check if character is underscore, if so transition to q5
            elif char =='_':
                state = 'q4'
            else:
                return False
            
        elif state == 'q4':
            ## after underscore, must have digit 0-7, transition back to q4
            if '0' <= char <= '7':
                state = 'q3'
            else:
                return False
            
    ##if we end in state q4, return True
    if state == 'q3':
        return True
    else:
        return False
