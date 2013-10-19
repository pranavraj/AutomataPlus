import os
def convertfile(StateList,Initial,Final,Filename):
    file_name = open(Filename,'w')
    num_states = len(StateList)
    num_letter = len(StateList[0].Transition)
    string = str(num_letter) + " " + str(num_states)+'\n'
    file_name.write(string)
    file_name.write('{')
    for state in Initial:
        file_name.write(str(state))
        file_name.write(',')
    file_name.seek(-1,os.SEEK_CUR)
    file_name.write('}'+'\n')
    for state in StateList:
        for trans in state.Transition:
            file_name.write('{')
            for transition in trans:
                file_name.write(str(transition))
                file_name.write(',')
            file_name.seek(-1,os.SEEK_CUR)
            file_name.write('}'+' ')
        file_name.seek(-1,os.SEEK_CUR)
        file_name.write('\n')
    file_name.write('{')
    for state in Final:
        file_name.write(str(state))
        file_name.write(',')
    file_name.seek(-1,os.SEEK_CUR)
    file_name.write('}'+'\n')
    file_name.close()

