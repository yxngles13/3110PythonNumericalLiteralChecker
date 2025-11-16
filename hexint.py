#check if valid hexinteger using nfa approach

#boolean function to check if hex integer
#cannot use int, float, s.isdigit, regex libraries
#can use for/while, if else, <= ‘0-9’

def is_hexint(s):

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
            #second state must be 'x' or 'X'
            if char == 'x' or char == 'X':
                state = 'q3'
            else:
                return False
            
        elif state == 'q3':
            ##check if character is a digit 0-9, a-f, A-F, if so loop
            if is_hexdigit(char):
                state = 'q3'
            ## check if character is underscore, if so transition to q4
            elif char =='_':
                state = 'q4'
            else:
                return False
            
            ## after underscore, must have digit 0-9, a-f, A-F, transition back to q3
        elif state == 'q4':
            if is_hexdigit(char):
                state = 'q3'
            else:
                return False
            
    ##if we end in accepting state q3, return True
    if state == 'q3':
        return True
    else:
        return False

#must have digit 0-9, a-f, A-F
def is_hexdigit(c):
    return ('0' <= c <= '9') or ('a' <= c <= 'f') or ('A' <= c <= 'F')

