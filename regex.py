def metachar_proc(met_regex, met_string, met_length):
    #metachar '?'
    if met_regex[1] == '?':
        if met_regex.startswith('.') is False:
            for count in range(1):
                if met_regex[0] == met_string[0]:
                    met_string = met_string[1:]
        else:
            if len(met_regex) == 2:
                return True
            for count in range(1):
                if met_regex[2] != met_string[0]:
                    met_string = met_string[1:]
    #metachar '*'
    elif met_regex[1] == '*':
        if met_regex.startswith('.') is False:
            while met_regex[0] == met_string[0]:
                met_string = met_string[1:]
        else:
            if len(met_regex) == 2:
                return True
            while met_regex[2] != met_string[0]:
                met_string = met_string[1:]
    #metachar '+'
    elif met_regex[1] == '+':
        if met_regex.startswith('.') is False:
            #if the first comparison is correct then you can go on else return False
            if met_regex[0] == met_string[0]:
                while met_regex[0] == met_string[0]:
                    met_string = met_string[1:]
            else:
                return False
        else:
            if len(met_regex) == 2:
                return True
            else:
    #slicing met_string from the last character that matches the character after the '+' metachar in the reg. ex.
                met_string = met_string[len(met_string) - (met_string[::-1].find(met_regex[2])) - 1:]
    return re(met_regex[2:], met_string, met_length)

def re(re_regex, re_string, original_regex_length):
    if len(re_regex) == 0 or (re_regex[0] == '$'):
        if len(re_regex) == 0:
            return True
        elif re_regex.startswith('$') and len(re_string) == 0:
            return True
        else:
            return False
    elif len(re_string) == 0:
        return False
    elif re_regex[0] == "\\":
        return re(re_regex[1:], re_string, original_regex_length - 1)
    elif len(re_regex) != 1 and re_regex[1] in ['?', '*', '+']:
        return metachar_proc(re_regex, re_string, original_regex_length)
        
    elif (re_regex[0] == '.') or (re_regex[0] == re_string[0]):
        return re(re_regex[1:], re_string[1:], original_regex_length)
    elif re_regex[0] != re_string[0]:
        if original_regex_length == len(re_regex):
            return re(re_regex, re_string[1:], original_regex_length)
        else:
            return False
    else:
        pass
        
def preconditioning_re(precon_regex, precon_string):
    precond_regex_length = len(precon_regex)
    if precon_regex.startswith('^') and precon_regex.endswith('$'):
        return re(precon_regex[1:], precon_string, precond_regex_length)
    if precon_regex.startswith('^'):
        return re(precon_regex[1:], precon_string, precond_regex_length)
    if precon_regex.endswith('$'):
        #[::-1] is for reversing a string
        precon_regex = precon_regex[::-1]
        return re(precon_regex[1:], precon_string[::-1], precond_regex_length)
    else:
        return re(precon_regex, precon_string, precond_regex_length)
        
def main():
    main_problem = input().split('|')
    main_regex = main_problem[0]
    main_string = main_problem[1]
    print(preconditioning_re(main_regex, main_string))

main()
