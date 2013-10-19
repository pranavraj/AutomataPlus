'''
Created on 08-Dec-2010

@author: Naman
'''
import string
alphadict = dict((i+1,x) for i, x in enumerate(string.ascii_lowercase))
alphadict[0] = '%'

def convert_to_dict(StateList):
    dict_FSA = {}
    for state in StateList:
        dict_list = []
        for index in range(len(state.Transition)):
            for next_state in state.Transition[index]:
                if(next_state == -1):
                    pass
                else:
                    trans_list = []
                    trans_list.append(alphadict[index])
                    trans_list.append(str(next_state))
                    dict_list.append(trans_list)
        dict_FSA[str(state.StateName)] = dict_list
    return dict_FSA