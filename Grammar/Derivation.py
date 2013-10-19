def Show_Rules(Grammar):
    String = "<html><body> <p> <font size= 5 face= 'Georgia, Arial' color= ' black ' >"
    count = 0
    dict_G = {}
    for state in Grammar.dict_grammar:
        for rule in Grammar.dict_grammar[state]:
            dict_G[(count,state)] = rule
            String = String + str(count) + " : " + state + " -> " + rule +" <br> "
            count += 1
    String += "<\font><\body><\html>"
    return String,dict_G

def Derivation(dictionary,rule_number,location,string):
    try:
        """
        print "Currently string is",string
        print "Rule number is ",rule_number
        print "location is",location
        print dictionary
        """
        string = string[:location] + dictionary[(rule_number,string[location])] + string[location+1:]
        return string
    except:
        return "Error"



