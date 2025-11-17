def is_floatingpoint(s):
  
    if len(s) == 0:
        return False
    
    state = 'q0'
    
    for char in s:
        if state == 'q0':
            if char in ['+', '-']:
                state = 'q1'
            elif char == '0':
                state = 'q2'
            elif '1' <= char <= '9':
                state = 'q3'
            elif char == '.':
                state = 'q4'
            else:
                return False
                
        elif state == 'q1':
            if char == '0':
                state = 'q2'
            elif '1' <= char <= '9':
                state = 'q3'
            elif char == '.':
                state = 'q4'
            else:
                return False
                
        elif state == 'q2':
            if char == '.':
                state = 'q5'
            elif char in ['e', 'E']:
                state = 'q6'
            else:
                return False
                
        elif state == 'q3':
            if '0' <= char <= '9':
                state = 'q3'
            elif char == '.':
                state = 'q5'
            elif char in ['e', 'E']:
                state = 'q6'
            else:
                return False
                
        elif state == 'q4':
            if '0' <= char <= '9':
                state = 'q4'
            else:
                return False
                
        elif state == 'q5':
            if '0' <= char <= '9':
                state = 'q5'
            elif char in ['e', 'E']:
                state = 'q6'
            else:
                return False
                
        elif state == 'q6':
            if char in ['+', '-']:
                state = 'q7'
            elif '0' <= char <= '9':
                state = 'q8'
            else:
                return False
                
        elif state == 'q7':
            if '0' <= char <= '9':
                state = 'q8'
            else:
                return False
                
        elif state == 'q8':
            if '0' <= char <= '9':
                state = 'q8'
            else:
                return False
        else:
            return False
    
    return state in ['q2', 'q3', 'q4', 'q5', 'q8']