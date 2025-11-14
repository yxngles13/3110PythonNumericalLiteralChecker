# checking if valid decinteger

#boolean function to check if decimal integer
#cannot use int, float, s.isdigit, regex libraries
#can use for/while, if else, <= ‘0-9’

def is_decint(c, state):

    ##if the length of input string is 0, return False
    if len(input) == 0:
        return False
    
    ##loop through each character in the string
    for char in input:
        ##check if the character is less than '0' or greater than '9'
        if char < '0' or char > '9':
            return False
    
