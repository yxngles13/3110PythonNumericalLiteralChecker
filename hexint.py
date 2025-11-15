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
            ##check if character is a digit 0-9, a-f, A-F
            if is_hexdigit(char):
                state = 'q2'
            else:
                return False
        elif state == 'q2':
            ##check if character is a digit 0-9, a-f, A-F
            if is_hexdigit(char):
                state = 'q2'
            ## check if character is underscore, if so transition to q3
            elif char =='_':
                state = 'q3'
            else:
                return False
            ## after underscore, must have digit 0-9, a-f, A-F, transition back to q2
        elif state == 'q3':
            if is_hexdigit(char):
                state = 'q2'
            else:
                return False
            
    ##if we end in state q2, return True
    if state == 'q2':
        return True
    else:
        return False
    
def is_hexdigit(c):
    return ('0' <= c <= '9') or ('a' <= c <= 'f') or ('A' <= c <= 'F')

