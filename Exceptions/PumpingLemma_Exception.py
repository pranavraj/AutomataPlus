'''
Created on 20-Dec-2010

@author: Naman
'''
class Length_less_than_n(Exception):
    def __init__(self,word,length):
        self.mssg = "The entered word has length less than "
        self.val = word
        self.val1 = length
    def __str__(self):
        string =  self.mssg + str(self.val1) + "\t" + self.val 
        return string
    
class WordNotInLang(Exception):
    def __init__(self,word,lang):
        self.mssg1 = "The entered word "
        self.mssg2 = " does not belong to the language "
        self.lang = lang
        self.word = word
        
    def __str__(self):
        string = self.mssg1 + self.word + self.mssg2 + self.lang
        return string

class IllegalInput(Exception):
    def __init__(self,x,y,n):
        if(y<1):
            self.mssg = "The length of value to be pumped cannot be less than 1 "
        else:
            self.mssg = "The sum of x and y has to be less than n"
        self.val1 = x
        self.val2 = y
        self.val3 = n
    def __str__(self):
        string =  self.mssg 
        return string