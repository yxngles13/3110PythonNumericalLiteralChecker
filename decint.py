# checking if valid decinteger

#boolean function to check if decimal integer
#cannot use int, float, s.isdigit, regex libraries
#can use for/while, if else, <= ‘0-9’

def is_decint(s):
    if len(s) == 0:
        return False

    state = 'q1'  # start

    for i, char in enumerate(s):
        if state == 'q1':
            if char == '0':
                # "0" alone is fine, but anything else after it is invalid
                state = 'q0'
            elif '1' <= char <= '9':
                state = 'q2'
            else:
                return False

        elif state == 'q0':
            # if we started with 0, no more characters allowed
            return False

        elif state == 'q2':
            if '0' <= char <= '9':
                state = 'q2'
            elif char == '_':
                # underscore must be followed by a digit
                # reject trailing underscores immediately
                if i == len(s) - 1:
                    return False
                state = 'q3'
            else:
                return False

        elif state == 'q3':
            # must have a digit after underscore
            if '0' <= char <= '9':
                state = 'q2'
            else:
                return False

    # Accepting states
    return state in ('q0', 'q2')
