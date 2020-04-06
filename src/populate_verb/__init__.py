terminal = ['1 p.s','2p.s','3p.s','1 p.p','2 p.p','3 p.p']
present_terminal = ['o','s','','mos','is','n']
tense = ['presente indicativo']

def populate_regular_verbs(spanish_verb,french_verb,person,term):
    if (person == 0):
        cut = 3
        current_verb = spanish_verb[0:len(spanish_verb) - cut]
        current_verb += term
        print(current_verb)
    elif (person == 4):
        if (spanish_verb[len(spanish_verb) - 3] == 'a'):
            cut = 3
            current_verb = spanish_verb[0:len(spanish_verb) - cut]
            current_verb += 'á' + term
        elif (spanish_verb[len(spanish_verb) - 3] == 'e'):
            cut = 3
            current_verb = spanish_verb[0:len(spanish_verb) - cut]
            current_verb += 'é' + term
        elif (spanish_verb[len(spanish_verb) - 3] == 'i'):
            cut = 3
            current_verb = spanish_verb[0:len(spanish_verb) - cut]
            current_verb += 'ís'
    else:
        cut = 2
        current_verb = spanish_verb[0:len(spanish_verb) - cut]
        current_verb += term
        print(current_verb)
    out_french_verb = french_verb + "(" + str(terminal[person]) + "-" + tense[0] + ")"
    return [current_verb,out_french_verb]