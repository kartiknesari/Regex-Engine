def metachar_proc(met_regex, met_string, met_length):
    """Scans the metacharacter in the regular expression and handles the string depending on the metacharacter involved.
    
    \ - an escape sequence metacharacter. Any character subceding the '\' is a normal character instead of a metacharacter.
    ? - a metacharacter that accepts chaaracter stream of size 0 or 1.
    * - a metacharacter that accepts zero or more stream of characters.
    + - a metacharacter that accepts one or more stream of characters
    . - wildcard, can designate any character or value"""
    #metachar '?'
    if met_regex[1] == '?':
        if met_regex.startswith('.') is False:
            for count in range(1):
                if met_regex[0] == met_string[0]:
                    met_string = met_string[1:]
        else:
        #below comparison is applicable for cases like - .?|aaa
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
"""A function that handles the strings recursively. This function scans the strings one character at a time. 
Info on perhaps unknown characters:-
. - wildcard, can designate any character or value"""
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
    #if no character has yet been sliced from regular expression then the reg. ex. is still usable.
    #do not use an reg. ex. sliced even once after preprocessing; return False as the answer,
    #otherwise you can get invalid answers for other strings and reg. ex.
        if original_regex_length == len(re_regex):
            return re(re_regex, re_string[1:], original_regex_length)
        else:
            return False
    else:
        pass
        
def preconditioning_re(precon_regex, precon_string):
"""Does some pre-processing on the regular expression before sending it to re() for checking like
Removal of ^, $ sign before forwarding the regex for checking.
The length of the regular expression is taken to later be compared with the (used) regular expression in re() 
Here,
^ - Start of the regular expression
$ - End of the regular expression"""

    precond_regex_length = len(precon_regex)
    if precon_regex.startswith('^') and precon_regex.endswith('$'):
    #only ^ is removed, $ remains
        return re(precon_regex[1:], precon_string, precond_regex_length)
    if precon_regex.startswith('^'):
    # ^ is removed, $ does not exist in this regex
        return re(precon_regex[1:], precon_string, precond_regex_length)
    if precon_regex.endswith('$'):
        #string[::-1] is for reversing a string
        #regex and string are revered for easier access to comparison of ending characters.
        precon_regex = precon_regex[::-1]
        return re(precon_regex[1:], precon_string[::-1], precond_regex_length)
    else:
        return re(precon_regex, precon_string, precond_regex_length)
        
def main():
"""This function accepts the input and splits them into two based on the index value of the pipe operator('|').
The two stringgs regex and the string to be checked is then passed to be preprocessed before its checking takes place."""
    main_problem = input().split('|')
    main_regex = main_problem[0]
    main_string = main_problem[1]
    print(preconditioning_re(main_regex, main_string))

main()
