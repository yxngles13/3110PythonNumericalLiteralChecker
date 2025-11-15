#check if valid hexinteger using nfa approach

#boolean function to check if hex integer
#cannot use int, float, s.isdigit, regex libraries
#can use for/while, if else, <= ‘0-9’

def is_hexint(s):

    ##if the length of input string is 0, return False
    if len(s) == 0:
        return False
    
    
