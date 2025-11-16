def isfloatingpoint(s):
    if len(s) == 0:
        return False
    state = 'q1'

    for char in s:
        if state == 'q1':
            #first state must be +, - or nothing
            if char == '+' or char == '-':
                state = 'q2'
            else:
                return False
        elif state == 'q2':
            if char == '.':
                state = 'q3'
            elif is_floatingpoint(char):
                state = 'q4'
            else:
                return False
        elif state == 'q3':
            if is_floatingpoint(char):
                state = 'q5'
            else:
                return False
        elif state == 'q4':
            if char == '.':
                state = 'q3'
            elif is_floatingpoint(char):
                state = 'q4'
            else:
                return False
        elif state == 'q5':
            if is_floatingpoint(char):
                state = 'q5'
            elif char == 'e' or char =='E':
                state = 'q6'
            else: False
        elif state == 'q6':
            if char == '+' or char == '-':
                state = 'q7'
            elif is_floatingpoint(char):
                state = 'q8'
            else:
                return False
        elif state == 'q7':
            if is_floatingpoint(char):
                state = 'q8'
            else:
                return False
        elif state == 'q8':
            if is_floatingpoint(char):
                state = 'q8'
            else:
                return False
    if state == 'q3' or state == 'q5' or state == 'q4' or state == 'q8':
        return True 
    else:
        return False 

def is_floatingpoint(c):
    return ('0' <= c <= '9')