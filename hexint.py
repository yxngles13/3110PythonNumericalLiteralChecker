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
            #q1 transition q2 if first character is 0
            if char == '0':
                state = 'q2'
            else:
                return False
        
        elif state == 'q2':
            #q2 transition to q3 if second character is 'x' or 'X'
            if char == 'x' or char == 'X':
                state = 'q3'
            else:
                return False
            
        elif state == 'q3':
            #check if character is a digit 0-9, a-f, A-F, if so transition to q4
            if is_hexdigit(char):
                state = 'q4'
            #check if character is underscore, if so transition to q5
            elif char =='_':
                state = 'q5'
            else:
                return False
        #q3 and q4 look the same but this prevents accepting 0x/0X

        #q4 is accept state
        elif state == 'q4':
            #check if character is a digit 0-9, a-f, A-F, if so loop
            if is_hexdigit(char):
                state = 'q4'
            #check if character is underscore, if so transition to q5
            elif char =='_':
                state = 'q5'
            else:
                return False
            
            #after underscore, must have digit 0-9, a-f, A-F, transition back to q4
        elif state == 'q5':
            if is_hexdigit(char):
                state = 'q4'
            else:
                return False
            
    ##if we end in accepting state q4, return True
    if state == 'q4':
        return True
    else:
        return False

#must have digit 0-9, a-f, A-F
def is_hexdigit(c):
    return ('0' <= c <= '9') or ('a' <= c <= 'f') or ('A' <= c <= 'F')

